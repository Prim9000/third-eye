from PIL import Image
import os
import numpy as np
from tesserocr import PyTessBaseAPI
import pytesseract
from PIL import Image
import cv2
from gtts import gTTS
from io import BytesIO
import time

vid = cv2.VideoCapture(0)
last_recorded_time = time.time() # this keeps track of the last time a frame was processed

while True:
    curr_time = time.time() # grab the current time
    ret, frame = vid.read()
    #operation on image, it's not important
    cv2.imshow('frame', frame)

    if curr_time - last_recorded_time >= 5.0: # it has been at least 2 seconds
        # NOTE: ADD SOME STATEMENTS HERE TO PROCESS YOUR IMAGE VARIABLE, img
        	
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, lang='eng+tha')
        print(text)
    
        if text:
            myOutput = gTTS(text=text, lang='tha')
            myOutput.save('talk.mp3')
            os.system('mpg123 talk.mp3')
        # IMPORTANT CODE BELOW
        last_recorded_time = curr_time
	
cv2.waitKey(0)
cv2.destroyAllWindows()