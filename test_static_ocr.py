from PIL import Image
import pytesseract

img = Image.open('p13a.png')

print pytesseract.image_to_string(img)