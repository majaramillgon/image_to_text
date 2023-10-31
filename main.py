import cv2
import pytesseract as ps
import os
import re

class Convert:
    def __init__(self, file):
        self.file = file
    
    def get_text(self):
        img = cv2.imread(self.file)
        #print(ps.image_to_string(img))
        a = ps.image_to_string(img)
        return a

doc = 'A1.png'

#str = Convert(doc).get_text().replace("\n", "")
str = Convert(doc).get_text()
print(str)
