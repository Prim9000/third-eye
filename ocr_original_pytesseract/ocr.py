from gtts import gTTS
import cv2
import os
from tesserocr import PyTessBaseAPI
from PIL import Image

vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    with PyTessBaseAPI(lang="tha") as api:
        # delete space
        api.SetVariable('preserve_interword_spaces', '1')

        api.SetImageFile(frame)
        print(api.GetUTF8Text())