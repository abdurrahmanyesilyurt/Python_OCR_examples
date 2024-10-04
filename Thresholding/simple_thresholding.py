import cv2
import numpy as np
import pytesseract

# Görüntü gösterme fonksiyonu
def show_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyWindow(window_name)

# Orijinal resmi yükle ve göster
img = cv2.imread('D:\PyProjects\pythonProject\Images\page-book.jpg')
show_image('Image', img)

# Gri tonlamaya çevir ve göster
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show_image('Image1', gray)

# Eşikleme işlemi - threshold 127
value, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
show_image('Image2', thresh1)

# Eşikleme işlemi - threshold 180
value, thresh2 = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
show_image('Image3', thresh2)

# Eşikleme işlemi - threshold 140
value, thresh3 = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
show_image('Image4', thresh3)
