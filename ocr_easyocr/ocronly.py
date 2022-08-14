# show an image
import PIL
from PIL import ImageDraw
import easyocr
import torch
from gtts import gTTS
from io import BytesIO
import cv2
import os
from playsound import playsound

im = PIL.Image.open("133040.jpg")
reader = easyocr.Reader(['th','en'])
#running the model find bounds and text
bounds = reader.readtext('133040.jpg')

texts = ""
for bound in bounds:
  texts += bound[1]
print(texts)