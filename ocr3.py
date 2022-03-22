import numpy as np
import cv2
import time
import pytesseract
import os
cap = cv2.VideoCapture(0)
#work
while(True):
    # Capture frame-by-frame
    start_time = time.time()
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    text = pytesseract.image_to_string(gray, lang='eng+tha')
    print(text)
    #time.sleep(5.0 - time.time() + start_time) # Sleep for 1 second minus elapsed time

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()