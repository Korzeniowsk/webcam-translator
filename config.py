#Tunable settings. DO NOT TOUCH OTHER FILES PLEASEEE

CAMERA_INDEX = 0 #for default webcam

OCR_LANGUAGES = ['en','hi'] #EasyOCR wants to detect only these two languages

TARGET_LANGUAGE = 'hi' #change it when required. Now set to hindi

TTS_LANGUAGE = 'hi' #change it when required. Now set to hindi

OCR_EVERY_N_FRAMES = 30 #for every 30 frames, OCR will be run. considering the fps of webcam, this is fine. this will also prevent lag

MIN_CONFIDENCE = 0.4 #EasyOCR confidence must be 0.4 or above for it to be shown

MIN_TEXT_LENGTH = 5 #before proceeding to translation and TTS, needs at least 5 characters. remember, 5 characters not words
