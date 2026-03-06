import easyocr
import cv2
import numpy as np
from config import OCR_LANGUAGES, MIN_CONFIDENCE

class OCRReader:
    def __init__(self):
        print("Loading EasyOCR model..be patient please!")

        self.reader = easyocr.Reader(OCR_LANGUAGES, gpu=False)

    def extract_text(self, preprocessed_frame):

        results = self.reader.readtext(preprocessed_frame)

        lines =[]
        boxes =[]

        for(bbox, text, confidence) in results:
            if confidence >= MIN_CONFIDENCE:
                lines.append(text.strip())
                boxes.append((bbox, text, confidence))

        full_text = ' '.join(lines)
        return full_text, boxes