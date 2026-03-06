## WEBCAM BASED TRANSLATOR
---------------------
This is a webcam based translator coded in python. It detects English and Devanagiri, translates the detected text to whichever language required (english to hindi or hindi to english) and speaks it out loud.

As an aspriring project manager, this project was a way for me to learn that software is a system of tradeoffs, not a list of features.

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
```
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

## Things I learned

- Knowing technical architecture matters: Initially when I had put it in ocr/preprocess.py, bounding box appeared only for ~33ms but when later changed it to ui/display.py it when the OCR was detecting the text (~1500ms). This feature led to the alteration of two files. Made me realise promising a feature requires knowledge of the pipeline and how much engineering prowess it takes

- Cons of third party dependencies: Intially I used googletrans for translation, but since it was not compatible with my python version (3.14), it broke the pipeline. Lesson learned: Third party dependencies are a liability. They show up in timelines, security reviews and maintenance costs

- OCR every frame VS OCR every 30th frame: Initially the video was freezing constantly. This was because OCR_EVERY_N_FRAME was not added in config file. I understood that smoother video was more important than fast detection, since text will not change that fast in current scenario

- Playsound repeating word in every detection: Adding self.last_text solved this so that if the consecutive next detection is the same as the one before, need not speak it out loud

- Structured system architecture: Debugging became ten times faster because this project had dedicated file pipeline and logic flow

- Try/Except: Apart from logic, dependencies can be external as well (internet speed, hardware etc). One failed translation due to something beyond your control should not lead to the entire translator shutting down. 

## Conclusion

I learned, broke and fixed a lot of things apart from the ones listed above. 

Hope you learn and have fun cloning or forking it :))
