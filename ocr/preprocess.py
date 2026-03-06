import cv2
import numpy as np

#preprocessing OCR feed for more occuracy of easyOCR.
#convert to grayscale => denoise => contrast_boost => threshold
#might change according to accuracy of results

def preprocess(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    denoised = cv2.fastNlMeansDenoising (gray, h=30)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrasted = clahe.apply(denoised)

    thresholded = cv2.adaptiveThreshold(contrasted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)

    return thresholded


