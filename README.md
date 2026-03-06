## WEBCAM BASED TRANSLATOR
---------------------
This is a webcam based translator coded in python. It detects English and Devanagiri, translates the detected text to whichever language required (english to hindi or hindi to english) and speaks it out loud.

## Features include:

- Real time detection using EsasyOCR (chosen over tesseract since Devanagiri is not supported in tesseract)
- Translates using Google Translate
- Speaks the translation out loud using gTTS
- Bounding boxes appear over the detected text
- Translated hindi text appears using Pillow and NotoSans Devanagiri font

## Project structure:
```
webcam_translator/
├── main.py
├── config.py
├── requirements.txt
├── assets/
│   └── NotoSansDevanagari_Condensed-Regular.ttf
├── capture/
│   └── camera.py
├── ocr/
│   ├── preprocess.py
│   └── reader.py
├── translation/
│   └── translator.py
├── tts/
│   └── speaker.py
├── ui/
│   └── display.py
└── utils/
    └── logger.py

## Installation:

- pip install -r requirements.txt (NOTE: observed that some heavy files like playsound and gTTS needs separate install commands. Please check before proceeding)

- python main.py

## Control buttons:
- 'q' for quitting application
- 'b' for bounding box ON/OFF

## Tech stack utilised in this project:

- OpenCV - python
- numpy
- EasyOCR
- deep_translator
- gTTS
- Pillow
- playsound
