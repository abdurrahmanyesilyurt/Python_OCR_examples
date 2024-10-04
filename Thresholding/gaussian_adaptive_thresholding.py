import cv2
import numpy as np
import pytesseract

def show_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyWindow(window_name)

img = cv2.imread('D:\PyProjects\pythonProject\Images/book_adaptative.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show_image('image',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
show_image('image1',adaptive_gaussian)
adaptive_average = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
show_image('image2',adaptive_average)