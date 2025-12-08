#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           pytesseract_example.py
Author:         Antonio Arteaga
Last Updated:   2025-11-12
Version:        1.0
Description:
Obtains text from a picture by using the pytesseract library and the 'tesseract' OCR engine.
The "tesseract.exe" must be installed. See documentation in:
'./documentation/Instalacion del Tesseract OCR.docx'
Dependencies:   pillow==12.0.0, pytesseract==0.3.13
"""

import pytesseract as tess
from PIL import Image

# For Windows
# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# For Linux
tess.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Load picture
img = Image.open('./data/raw/example1.png')

# Extract text
texto = tess.image_to_string(img, lang='eng')
print(texto)
