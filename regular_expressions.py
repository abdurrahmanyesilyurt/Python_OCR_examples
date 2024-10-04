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

img = cv2.imread('Images/table_test.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Image', rgb)
cv2.waitKey(0)  # Bir tuşa basılana kadar bekle
cv2.destroyWindow('Image')  # İlk pencereyi kapat
result = pytesseract.image_to_data(rgb, config='--psm 6', lang='por', output_type=Output.DICT)
date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
dates = []
min_confidence = 40
img_copy = rgb.copy()
for i in range(0, len(result['text'])):
  confidence = int(result['conf'][i])
  if confidence > min_confidence:
    text = result['text'][i]
    if re.match(date_pattern, text):
      x, y, img = bouding_box(result, img_copy, i, (0,0,255))
      #cv2.putText(img_copy, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,0,255))
      img_copy = write_text(text, x, y, img_copy, font, 12)
      dates.append(text)
    else:
      x, y, img_copy = bouding_box(result, img_copy, i)
cv2.imshow('Image1', img_copy)
cv2.waitKey(0)  # Bir tuşa basılana kadar bekle
cv2.destroyAllWindows()  # Tüm pencereleri kapat

print(dates)