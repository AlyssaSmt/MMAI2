import os
import json
from pathlib import Path

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data" / "images"
MODELS_DIR = BASE_DIR.parent / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

IMG_SIZE = 28
BATCH_SIZE = 64
EPOCHS = 15

def create_generators():
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Datenordner nicht gefunden: {DATA_DIR}")

    datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        validation_split=0.2
    )

    train_gen = datagen.flow_from_directory(
        DATA_DIR,
        target_size=(IMG_SIZE, IMG_SIZE),
        color_mode="grayscale",
        class_mode="categorical",
        batch_size=BATCH_SIZE,
        subset="training",
        shuffle=True
    )

    val_gen = datagen.flow_from_directory(
        DATA_DIR,
        target_size=(IMG_SIZE, IMG_SIZE),
        color_mode="grayscale",
        class_mode="categorical",
        batch_size=BATCH_SIZE,
        subset="validation",
        shuffle=False
    )

    return train_gen, val_gen

def build_model(input_shape, num_classes):
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(32, (3, 3), activation="relu", padding="same"),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu", padding="same"),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation="relu", padding="same"),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

def main():
    print(f"Verwende Daten aus: {DATA_DIR}")

    train_gen, val_gen = create_generators()

    num_classes = train_gen.num_classes
    class_indices = train_gen.class_indices

    input_shape = (IMG_SIZE, IMG_SIZE, 1)
    model = build_model(input_shape, num_classes)

    model.summary()

    history = model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=EPOCHS
    )

    model_path = MODELS_DIR / "quickdraw_cnn.h5"
    model.save(model_path)
    print(f"Modell gespeichert unter: {model_path}")

    index_to_class = {idx: cls for cls, idx in class_indices.items()}

    mapping_path = MODELS_DIR / "class_indices.json"
    with open(mapping_path, "w", encoding="utf-8") as f:
        json.dump(index_to_class, f, ensure_ascii=False, indent=2)

    print(f"Klassenmapping gespeichert unter: {mapping_path}")

if __name__ == "__main__":
    main()
