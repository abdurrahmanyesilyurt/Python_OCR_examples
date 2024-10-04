import pytesseract
import numpy as np
import cv2  # openCV

# Tesseract'ın yolunu belirtiyoruz

img = cv2.imread('Images/exit.jpg')

# İlk resmi göster ve bir tuşa basılmasını bekle
cv2.imshow('Image', img)
cv2.waitKey(0)  # Bir tuşa basılana kadar bekle
cv2.destroyWindow('Image')  # İlk pencereyi kapat

# İkinci resmi göster ve kapatmayı bir tuş basımına bağlı yap
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Image1', rgb)
cv2.waitKey(0)  # Bir tuşa basılana kadar bekle

text = pytesseract.image_to_string(rgb, config='--psm 6')
print(text)
cv2.destroyAllWindows()  # Tüm pencereleri kapat

