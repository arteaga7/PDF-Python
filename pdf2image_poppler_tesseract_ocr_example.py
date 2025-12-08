#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           pdf2image_poppler_tesseract_ocr_example.py
Author:         Antonio Arteaga
Last Updated:   2025-11-19
Version:        1.0
Description:
Text is obtained from a PDF file by using the pdf2image (with poppler) libraries and tesseract_ocr.
The PDF file can contain flat text and pictures, RECOMMENDED FOR SCANNED PDFs.
All text is saved in "output_txt".
Dependencies:   pdf2image==1.17.0, pytesseract==0.3.13, pillow==12.0.0, numpy==2.2.6,
'poppler-25.07.0' and 'tesseract_ocr' installed.
"""

from pdf2image import convert_from_path
import pytesseract as tess
from matplotlib import pyplot as plt

pdf_path = "./data/raw/text_and_img.pdf"
output_txt = "./pdf2image_poppler_tesseract_ocr_text.txt"

# For Windows
# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# For Linux
tess.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Convert PDF to images (for Windows)
# pages = convert_from_path(pdf_path, dpi=200, poppler_path=r"/usr/bin/poppler")

# Convert PDF to images (for Linux)
pages = convert_from_path(pdf_path, dpi=200)
texto_total = ""


for i, page in enumerate(pages):
    print(f"Processing page {i+1}/{len(pages)}...")

    # Perform OCR
    texto = tess.image_to_string(
        page, lang='eng')               # lang='spa' for Spanish
    texto_total += f"\n--- PAGE {i+1} ---\n"
    texto_total += texto + "\n"

# Save the text in a file
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(texto_total)

print(f"Text saved in {output_txt}")
