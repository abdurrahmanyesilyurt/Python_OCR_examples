import re # regular expressions
import pytesseract
import numpy as np
import cv2  # openCV
from pytesseract import Output
from PIL import ImageFont, ImageDraw, Image
font = 'calibri.ttf'

def write_text(text, x, y, img, font, font_size = 32):
  font = ImageFont.truetype(font, font_size)
  img_pil = Image.fromarray(img)
  draw = ImageDraw.Draw(img_pil)
  draw.text((x, y - font_size), text, font = font)
  img = np.array(img_pil)
  return img

def bouding_box(result, img, i, color = (255,100,0)):
  x = result['left'][i]
  y = result['top'][i]
  w = result['width'][i]
  h = result['height'][i]

  cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

  return x, y, img
img = cv2.imread('Images/cup.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
config_tesseract = "--tessdata-dir D:/Tesseract/tessdata --psm 11"
result = pytesseract.image_to_data(rgb, config=config_tesseract, lang = 'eng', output_type=Output.DICT)
min_confidence = 40
img_copy = rgb.copy()
for i in range(0, len(result['text'])):
  confidence = int(result['conf'][i])
  if confidence > min_confidence:
    text = result['text'][i]
    if not text.isspace() and len(text) > 0:
      x, y, img = bouding_box(result, img_copy, i)
      cv2.putText(img_copy, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,0,255))
cv2.imshow('Image', img_copy)
cv2.waitKey(0)