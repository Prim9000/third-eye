from PIL import Image
import cv2
import numpy as np
from tesserocr import PyTessBaseAPI
from PIL import Image
import cv2
import time

cam=cv2.VideoCapture(0)
last_recorded_time = time.time() # this keeps track of the last time a frame was processed

while True:
    curr_time = time.time() # grab the current time

    # keep these three statements outside of the if statement, so we 
    #     can still display the camera/video feed in real time
    suc, img=cam.read()
    #operation on image, it's not important
    cv2.imshow('frame', img)

    if curr_time - last_recorded_time >= 5.0: # it has been at least 2 seconds
        # NOTE: ADD SOME STATEMENTS HERE TO PROCESS YOUR IMAGE VARIABLE, img
        	
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, lang='eng+tha')
        print(text)
        # IMPORTANT CODE BELOW
        last_recorded_time = curr_time
	
cv2.waitKey(0)
cv2.destroyAllWindows()