import json
import numpy as np
from PIL import Image
from pathlib import Path
import tensorflow as tf

IMG_SIZE = 64

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "quickdraw_cnn.keras"
CLASSES_PATH = BASE_DIR / "models" / "class_indices.json"

TEST_IMAGE = BASE_DIR / "data" / "images" / "full_simplified_sun" / "full_simplified_sun_00006.png"

model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASSES_PATH, "r", encoding="utf-8") as f:
    index_to_class = json.load(f)

img = Image.open(TEST_IMAGE).convert("L")
img = img.resize((IMG_SIZE, IMG_SIZE))
arr = np.array(img) / 255.0
x = arr.reshape(1, IMG_SIZE, IMG_SIZE, 1)

preds = model.predict(x)[0]
top = preds.argsort()[-5:][::-1]

print("Top-5:")
for i in top:
    print(index_to_class[str(i)], round(float(preds[i]), 3))
