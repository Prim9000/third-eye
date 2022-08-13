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

#tts
tts = gTTS(text=texts, lang= 'th')
tts.save('1.wav') #save the string converted to speech as a .wav file
sound_file = '1.wav'
#Audio(sound_file, autoplay=True) 
# for playing note.wav file
playsound('1.wav')
print('playing sound using  playsound')

#myOutput = gTTS(text=texts, lang='th')
#myOutput.save('talk.mp3')
#os.system('mpg123 talk.mp3')
  

# Draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(im, bounds)