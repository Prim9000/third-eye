from PIL import Image
import cv2
import numpy as np
from tesserocr import PyTessBaseAPI
from PIL import Image

im = Image.open("Image.jpeg")
im_gray = im.convert("L")


kernel = np.ones((3,3), np.uint8) 
conv_img = np.array(im_gray) 
new_img = cv2.erode(conv_img, kernel, iterations=1)
#new_img = cv2.dilate(conv_img, kernel, iterations=1)

text = pytesseract.image_to_string(new_img, lang='eng+tha')
print(text)