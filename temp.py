import pytesseract

from PIL import Image

import pyttsx3

img = Image.open('C:/Users/admin/Desktop/abc.jpg')

print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)

engine = pyttsx3.init()

# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(result)
engine.runAndWait()
