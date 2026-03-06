import cv2
import threading
from capture.camera import Camera
from ocr.preprocess import preprocess
from ocr.reader import OCRReader
from translation.translator import TextTranslator
from tts.speaker import Speaker
from ui.display import draw_overlay
from ui.display import draw_bounding_boxes
from utils.logger import get_logger
from config import OCR_EVERY_N_FRAMES, MIN_TEXT_LENGTH

logger=get_logger("main")


def speak_async(speaker, text):
    thread =  threading.Thread(target=speaker.speak, args=(text,))
    thread.daemon = True
    thread.start()

def main():
    camera=Camera()
    ocr = OCRReader()
    translator = TextTranslator()
    speaker = Speaker()
    draw_boxes = False
    current_boxes = []

    frame_count = 0
    current_original = ""
    current_translated = ""

    logger.info("As you wish! Starting webcam translator. Press 'q' to get out of here lol")

    while True:
        frame = camera.get_frame()
        if frame is None:
            break

        frame_count +=1

        if frame_count % OCR_EVERY_N_FRAMES == 0:
            preprocessed = preprocess(frame)
            detected_text, current_boxes = ocr.extract_text(preprocessed)

            if len(detected_text) >= MIN_TEXT_LENGTH:
                #logger.info(f"Detected: {detected_text}")
                translated = translator.translate(detected_text)

                if translated:
                    #logger.info(f"Translated: {translated}")
                    current_original = detected_text
                    current_translated = translated
                    speak_async(speaker, translated)

        if draw_boxes:
            frame = draw_bounding_boxes(frame, current_boxes)

          
        display_frame = draw_overlay(frame, current_original, current_translated)
        cv2.imshow("Webcam Translator!!", display_frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

        if key == ord('b'):
            draw_boxes = not draw_boxes
            logger.info(f"Bounding boxes: {'ON'if draw_boxes else 'OFF'}")
    
    camera.release()
    
    logger.info("Exited cleanly.")

if __name__ == "__main__":
    main()
