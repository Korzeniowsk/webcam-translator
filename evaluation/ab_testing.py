import cv2
import time
from ocr.reader import OCRReader
from ocr.preprocess import preprocess

def config_a(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=30)
    clahe = cv2.createCLAHE(clipLimit=2.0, timeGridSize=(8,8))
    contrasted = clahe.apply(denoised)
    thresholded = cv2.adaptiveThreshold(contrasted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresholded 

def config_b(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=30)
    thresholded = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded

def run_ab_test(image_path, truth):
    from ocr_evaluate import OCREvaluator
    frame = cv2.imread(image_path)
    ocr = OCRReader()
    evaluator = OCREvaluator()

    t0 = time.time()
    preprocess_a = config_a(frame)
    text_a, _ = ocr.extract_text(preprocess_a)
    latency_a = (time.time() - t0) * 1000
    result_a = evaluator.log_result(truth, text_a, latency_a)

    t0 = time.time()
    preprocess_b = config_b(frame)
    text_b, _ = ocr.extract_text(preprocess_b)
    latency_b = (time.time() - t0) * 1000
    result_b = evaluator.log_result(truth, text_b, latency_b)

    print("\n A/B TEST RESULTS")
    print(f"Config A => CER: {result_a['cer']:.2%} || WER: {result_a['wer']:.2%} || Latency: {latency_a:.0f}ms")
    print(f"Config B => CER: {result_b['cer']:.2%} || WER: {result_b['wer']:.2%} || Latency: {latency_b:.0f}ms")

    winner = "A" if result_a['cer'] <  result_b['cer'] else "B"
    print(f"\nWinner: Config {winner} (lower CER)")


    

