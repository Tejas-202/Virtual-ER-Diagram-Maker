import cv2
from PIL import Image
import pytesseract

camera = cv2.VideoCapture(0)
camera.set(3, 1280)
camera.set(4, 780)

while True:
    _, image = camera.read()
    cv2.imshow('Problem Statement ', image)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('que.jpg', image)
        break
camera.release()
cv2.destroyAllWindows()

def ter():
    pytesseract.pytesseract.tesseract_cmd = 'd:/Tesseract-OCR/tesseract.exe'
    img = Image.open("que.jpg")
    result1 = pytesseract.image_to_string(img)
    print(result1)
    return result1