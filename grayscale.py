import cv2
import numpy as np
import pytesseract

img = cv2.imread('Images/img-process.jpg')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyWindow('Image')
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image1', gray)
cv2.waitKey(0)
cv2.destroyWindow('Image1')
print(gray.shape)