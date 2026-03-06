import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import os

FONT_PATH = os.path.join(os.path.dirname(__file__), '..','assets','NotoSansDevanagari_Condensed-Regular.ttf')
FONT_LARGE = ImageFont.truetype(FONT_PATH, 20)
FONT_SMALL = ImageFont.truetype(FONT_PATH, 18)

def draw_bounding_boxes(frame, boxes):
    if not boxes:
        return frame
    
    for (bbox, text, confidence) in boxes:
        pts = [(int(p[0]), int(p[1])) for p in bbox]

        cv2.polylines(frame, [np.array(pts)], isClosed=True, color=(0,255,0), thickness=2)

        cv2.putText(frame, f"{confidence: .2f}", (pts[0][0], pts[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
    return frame

def draw_text_pil(frame, text, position, font, color=(255,255,255)):

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    draw = ImageDraw.Draw(pil_img)
    draw.text(position, text, font=font, fill=color)

    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

def draw_overlay(frame, original_text, translated_text):

    h,w=frame.shape[:2]
    overlay = frame.copy()

    cv2.rectangle(overlay,(0,h-120),(w,h),(0,0,0),-1)
    cv2.addWeighted(overlay, 0.6,frame,0.4,0,frame)

    cv2.putText(frame,f"Detected: {original_text[:60]}",(10,h-80), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),2)
    

    frame=draw_text_pil(frame, f"Translated: {translated_text[:40]}",(10,h-40),FONT_LARGE, color=(0,255,100))


    return frame