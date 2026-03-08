## WEBCAM BASED TRANSLATOR
---------------------
This is a webcam based translator coded in python. It detects English and Devanagiri, translates the detected text to whichever language required (english to hindi or hindi to english) and speaks it out loud.

As an aspiring project manager, this project was a way for me to learn that software is a system of tradeoffs, not a list of features. I built this to understand how engineering decisions translate into product decisions

## Demo:


## Quick start:

For live translator: 
- pip install -r requirements.txt 
- python main.py

For evaluation framework:
- python evaluation/run_evaluation.py
(Run `evaluation/run_evaluation.py` with test images to generate a report measuring WER, CER, and latency. Results are saved to `evaluation/report.json`.)

Press:
- 'q' for quitting application
- 'b' for bounding box ON/OFF

## Features include:

- Real time detection using EasyOCR (chosen over tesseract since Devanagiri is not supported in tesseract)
- Translates using Google Translate
- Speaks the translation out loud using gTTS
- Bounding boxes appear over the detected text
- Translated hindi text appears using Pillow and NotoSans Devanagiri font

## Evaluation framework
- CER/WER => measures OCR accuracy against actual truth
- Latency tracking => measures preprocessing, OCR and translation speed
- MOS scoring => User evaluates TTS audio quality
- A/B Testing => compared preprocessing configs quantitatively

## Project structure:
```
webcam_translator/
├── evaluation/               
│   ├── ocr_evaluate.py      <= WER, latency
│   ├── mos_evaluate.py      <= MOS scoring
│   └── ab_testing.py        <= A/B testing
├── main.py
├── config.py
├── requirements.txt
├── assets/
│   └──NotoSansDevanagari_Condensed-Regular.ttf
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
└── test_images/
   └── (add your test images here)
```


## Tech stack utilised in this project:

- OpenCV - python
- numpy
- EasyOCR
- deep_translator
- gTTS
- Pillow
- playsound

## Things I learned

- Knowing technical architecture matters: Initially when I had put it in ocr/preprocess.py, bounding box appeared only for ~33ms but when later changed it to ui/display.py it matches when the OCR was detecting the text (~1500ms). This feature led to the alteration of two files. Made me realise promising a feature requires knowledge of the pipeline and how much engineering prowess it takes

- Cons of third party dependencies (Speed to market vs. long-term reliability): Initially I used googletrans for translation, but since it was not compatible with my python version (3.14), it broke the pipeline. Lesson learned: Third party dependencies are a liability. They show up in timelines, security reviews and maintenance costs. This error in real life product deployment is a timeline hit and a maintenance cost. I switched to deep_translator; a lesson in vetting dependencies before committing to them.

- OCR every frame VS OCR every 30th frame (User experience vs. accuracy): Initially the video was freezing constantly. This was because OCR_EVERY_N_FRAME was not added in config file. I understood that smoother video was more important than fast detection, since text will not change that fast in current scenario. A freezing video breaks the user experience entirely; a slightly slower detection doesn't. Shipping a smooth, usable product beats shipping a "smarter" broken one.

- Playsound repeating word in every detection (Accuracy vs. user annoyance): Adding self.last_text solved this so that if the consecutive next detection is the same as the one before, need not speak it out loud

- Structured system architecture: Debugging became ten times faster because this project had dedicated file pipeline and logic flow

- Try/Except (Strictness vs. resilience): Apart from logic, dependencies can be external as well (internet speed, hardware etc). One failed translation due to something beyond your control should not lead to the entire translator shutting down. 

### Next steps

**Short Term (Low effort, high impact)**

- Replace gTTS with Sarvam's Bulbul API: Higher quality Hindi TTS with 
Indian language nuances and multiple voice options
- Replace deep-translator with Sarvam's translation API: Better handling 
of Indian language context and code switching (Hinglish)
- Add more Indian languages: Sarvam supports 11 languages including Tamil,
Telugu, Kannada, Bengali — extend beyond Hindi
- Export evaluation reports as CSV: Easier analysis in Excel or Google Sheets

**Medium Term (Moderate effort)**

- Add ASR (speech input): Instead of only reading text from camera, accept 
voice input and translate spoken words; completing the full ASR → translate → 
TTS pipeline
- GUI with Tkinter: language selector dropdown, settings panel, live metric 
display; no need to edit config.py manually
- Improve preprocessing pipeline: experiment with more configurations in 
A/B framework to systematically improve CER and WER
- Automated evaluation pipeline: Run evaluation automatically on a test 
dataset and generate comparison reports across versions

## Conclusion

This project didn't just polish my coding skills; it taught me to think in tradeoffs. Every freezing frame, broken dependency, and misplaced function was a product decision in disguise. If you clone this, I hope you break it a little. That's where the learning lives.
