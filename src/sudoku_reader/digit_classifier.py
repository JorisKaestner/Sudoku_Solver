# digit_classifier.py
import os
import numpy as np
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")
from tensorflow import keras

class DigitClassifier:
    """Loads a Keras MNIST classifier model from path to predict digits"""
    def __init__(self, model_path: str = "src/sudoku_reader/models/font_digit_model.keras"):
        self.model = keras.models.load_model(model_path)

    def classify(self, cell: np.ndarray) -> int:
        """cell: 28x28 grayscale array, values 0-255 (uint8 or float)."""
        normalized = cell.astype("float32") / 255.0
        input_batch = normalized.reshape(1, 28, 28)  # batch of 1
        prediction = self.model.predict(input_batch, verbose=0)
        return int(np.argmax(prediction))
