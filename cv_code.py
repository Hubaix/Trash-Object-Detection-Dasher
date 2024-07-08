#pip install ultralytics
#pip install opencv-python-headless



import cv2
from ultralytics import YOLO


#------- LOAD MODEL CODE:


model = YOLO('torch_optimized_model.pt')  

# inference:

model.predict(source=0, show=True)

