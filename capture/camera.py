import cv2
from config import CAMERA_INDEX

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        if not self.cap.isOpened():
            print("No webcam found :((")
        
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("No more frames :(")
        return frame
    
    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()