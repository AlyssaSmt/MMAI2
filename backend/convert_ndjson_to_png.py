"""
Konvertiert QuickDraw NDJSON-Dateien (Roh-Striche) zu Bilder (PNG).
Legt pro Klasse automatisch ein Verzeichnis an.

Erwartete Ordnerstruktur:
data/images/
    full_raw_arm.ndjson
    full_raw_bridge.ndjson
    ...

Ergebnis:
data/images/arm/arm_00001.png
data/images/arm/arm_00002.png
data/images/bridge/bridge_00001.png
...
"""

import json
import os
from pathlib import Path
from PIL import Image, ImageDraw

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data" / "ndjson"

OUTPUT_SIZE = 28  # Größe der Bilder


def draw_strokes(strokes, size=OUTPUT_SIZE):
    """
    Wandelt QuickDraw-Striche in ein PIL-Bild um.
    """
    img = Image.new("L", (256, 256), 255)  # groß anfangen
    draw = ImageDraw.Draw(img)

    for stroke in strokes:
        xs = stroke[0]
        ys = stroke[1]
        points = list(zip(xs, ys))
        draw.line(points, fill=0, width=8)

    # Normalisieren auf 28x28
    img = img.resize((size, size))
    return img


def convert_ndjson(file_path):
    name = file_path.stem.replace("full_raw_", "")
    output_dir = DATA_DIR.parent / "images" / name
    output_dir.mkdir(exist_ok=True)

    print(f"Konvertiere {file_path.name} → {output_dir}")

    with open(file_path, "r") as f:
        for i, line in enumerate(f):
            if i >= 2000:  # Anzahl begrenzen (optional)
                break

            sample = json.loads(line)
            strokes = sample["drawing"]

            img = draw_strokes(strokes)
            img.save(output_dir / f"{name}_{i:05}.png")


def main():
    ndjson_files = list(DATA_DIR.glob("*.ndjson"))

    if not ndjson_files:
        print("Keine NDJSON-Dateien gefunden.")
        return

    for file in ndjson_files:
        convert_ndjson(file)

    print("Fertig! Alle NDJSON-Dateien wurden konvertiert.")


if __name__ == "__main__":
    main()
