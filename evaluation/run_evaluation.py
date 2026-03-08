import sys
import os
import time
import cv2

# Add project root to path so imports work
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ocr.reader import OCRReader
from ocr.preprocess import preprocess
from evaluation.ocr_evaluate import OCREvaluator

def run():
    ocr = OCRReader()
    evaluator = OCREvaluator()


    test_cases = [
        ("test_images/test1.jpg", "HELLO WORLD"),
        ("test_images/test2.jpg", "नमस्ते दुनिया"),
        ("test_images/test3.jpg", "THIS IS A TEST"),
    ]

    for image_path, truth in test_cases:
        print(f"\nTesting: {image_path}")
        print(f"Truth: {truth}")

        
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Could not read image: {image_path}")
            continue

        
        t0 = time.time()
        preprocessed = preprocess(frame)
        preprocess_latency = (time.time() - t0) * 1000

        t1 = time.time()
        detected_text, _ = ocr.extract_text(preprocessed)
        ocr_latency = (time.time() - t1) * 1000

        total_latency = preprocess_latency + ocr_latency

        print(f"Detected:  {detected_text}")
        print(f"Preprocess latency: {preprocess_latency:.0f}ms")
        print(f"OCR latency: {ocr_latency:.0f}ms")
        print(f"Total latency: {total_latency:.0f}ms")

        # Log result
        result = evaluator.log_result(truth, detected_text, total_latency)
        print(f"CER: {result['cer']:.2%}")
        print(f"WER: {result['wer']:.2%}")

    # Save final report
    print("\nFINAL REPORT")
    evaluator.save_report()

if __name__ == "__main__":
    run()
