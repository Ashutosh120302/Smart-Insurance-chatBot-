import pytesseract
import cv2
from PIL import Image


# Load image
image_path = 'download (1).jfif'
image = cv2.imread(image_path)

# Convert to grayscale and apply OCR
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)

