# model_trainer.py
from PIL import Image, ImageDraw, ImageFont
from tensorflow import keras
import numpy as np
import random

FONTS = ["arial.ttf", "times.ttf"]  # basic fonts to generate synthetic dataset

def generate_printed_digit(digit: int, font_path: str, size: int = 28, jitter: bool = True) -> np.ndarray:
    """Generate synthetic training set"""
    img = Image.new("L", (size, size), color=0)
    draw = ImageDraw.Draw(img)
    font_size = int(size * random.uniform(0.65, 0.85)) if jitter else int(size * 0.75)
    font = ImageFont.truetype(font_path, size=font_size)
    bbox = draw.textbbox((0, 0), str(digit), font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - w) / 2 + (random.randint(-2, 2) if jitter else 0)
    y = (size - h) / 2 + (random.randint(-2, 2) if jitter else 0)
    draw.text((x, y), str(digit), fill=255, font=font)
    return np.array(img)

def build_model() -> keras.Model:
    """Defines the CNN architecture used for digit classification."""
    model = keras.Sequential([
        keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
        keras.layers.Conv2D(32, (3, 3), activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation="relu"),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(10, activation="softmax"),
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model


def train_font_classifier(
    save_model_path: str = "src/sudoku_reader/models/font_digit_model.keras",
    epochs: int = 5,
) -> None:
    """Trains model on synthetic dataset and saves to path"""
    (mnist_x, mnist_y), _ = keras.datasets.mnist.load_data()
    mnist_x = mnist_x.astype("float32") / 255.0

    synthetic_x, synthetic_y = [], []
    for digit in range(1, 10):
        for font_path in FONTS:
            for _ in range(300):
                synthetic_x.append(generate_printed_digit(digit, font_path))
                synthetic_y.append(digit)

    combined_x = np.concatenate([mnist_x, synthetic_x])
    combined_y = np.concatenate([mnist_y, synthetic_y])

    model = build_model()
    model.fit(combined_x, combined_y, epochs=epochs, validation_split=0.1)
    model.save(save_model_path)

def train_mnist_classifier(save_model_path:str="src/sudoku_reader/models/mnist_digit_model.keras"):
    """Loads Tensorflow mnist dataset and saves pre-trained model to path."""
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

train_font_classifier()
train_mnist_classifier()