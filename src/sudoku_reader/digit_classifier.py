# digit_classifier.py
import numpy as np
from tensorflow import keras

class DigitClassifier:
    """Loads a Keras MNIST classifier model from path to predict digits"""
    def __init__(self, model_path: str = "src/sudoku_reader/digit_model.keras"):
        self.model = keras.models.load_model(model_path)

    def classify(self, cell: np.ndarray) -> int:
        """cell: 28x28 grayscale array, values 0-255 (uint8 or float)."""
        normalized = cell.astype("float32") / 255.0
        input_batch = normalized.reshape(1, 28, 28)  # batch of 1
        prediction = self.model.predict(input_batch, verbose=0)
        return int(np.argmax(prediction))

def train_classifier(save_model_path:str):
    """Loads Tensorflow dataset and saves pre-trained model to path."""
    (x_train, y_train), _ = keras.datasets.mnist.load_data()
    x_train = x_train.astype("float32") / 255.0

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dense(10, activation="softmax"),
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=5)
    model.save(save_model_path)
