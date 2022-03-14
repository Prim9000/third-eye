import torch
from gtts import gTTS
from io import BytesIO
import cv2
import os

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

    # Model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    # Inference
    results = model(frame)

    df = results.pandas().xyxy[0]

    # Speak the labels
    labels = ""

    for label in df['name']:
      labels += label + " "
    
    if labels != "":
      myOutput = gTTS(text=labels, lang='en')
      myOutput.save('talk.mp3')
      os.system('mpg123 talk.mp3')
cv2.destroyAllWindows()
