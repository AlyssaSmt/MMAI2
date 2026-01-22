# MMAI2 – Montagsmaler mit KI (CNN + CLIP)

MMAI2 ist die zweite Version des Projekts *Montagsmaler mit KI* und baut direkt auf MMAI auf.  
Neben einem selbst trainierten **CNN-Modell** wird hier zusätzlich ein **CLIP-Modell** eingesetzt, um **Zero-Shot Recognition** zu ermöglichen.

Ziel des Projekts ist es, die Grenzen eines klassischen CNNs bei einer größeren Anzahl an Klassen zu untersuchen und dieses mit einem vortrainierten Vision-Language-Modell zu vergleichen.

---

## Features

- Zeichnen im Browser (HTML5 Canvas)
- KI-Vorhersagen durch zwei Modelle:
  - CNN (trainierte Klassen, ca. 30 Begriffe)
  - CLIP (Text–Bild-Vergleich, Zero-Shot)
- Anzeige von Konfidenzwerten
- Top-1- und Top-3-Vorhersagen
- Vergleich der Ergebnisse von CNN und CLIP
- Speichern von Zeichnungen inkl. Modellvorhersagen
- Galerie mit gespeicherten Ergebnissen

---

## Verwendete Technologien

- **TensorFlow / Keras** – Training des CNN
- **FastAPI** – Backend und Modell-Inferenz
- **Python** – Datenverarbeitung, Training und Backend-Logik
- **HTML / CSS / JavaScript** – Frontend
- **Google Quick, Draw! Dataset** – Trainingsdaten für das CNN
- **OpenAI CLIP** – Zero-Shot Image–Text Matching
- **PyTorch** – Ausführung des CLIP-Modells

---

## Quick Draw! NDJSON-Dateien hinzufügen

Die **NDJSON-Dateien des Quick Draw!-Datensatzes müssen manuell heruntergeladen und eingefügt werden**, da sie aus Größengründen nicht im Repository enthalten sind.

Lade die gewünschten Kategorien von:  
https://github.com/googlecreativelab/quickdraw-dataset

Die verwendeten Kategorien müssen mit den in `class_indices.json` definierten Klassen übereinstimmen.  
Es können auch andere Kategorien verwendet werden, sofern `class_indices.json` entsprechend angepasst wird.

Die NDJSON-Dateien müssen im folgenden Ordner abgelegt werden:



## How to get started

1. Virtuelle Umgebung erstellen und aktivieren
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate    # macOS / Linux
```
2. Abhängigkeiten installieren
```bash
    pip install -r requirements.txt
```
3. NDJSON → Bilder konvertieren
```bash
    cd backend
    python convert_ndjson_to_png.py
```
4. KI trainieren
```bash
    python train_model.py
```
5. Backend starten (FastAPI)
```bash
    uvicorn backend.main:app --reload --port 8002
```
Test (optional):
    Browser öffnen:
    http://127.0.0.1:8002/docs

6. Frontend starten
```bash
    frontend/index.html
```

