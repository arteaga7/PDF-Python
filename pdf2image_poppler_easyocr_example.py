#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           pdf2image_poppler_easyocr_example.py
Author:         Antonio Arteaga
Last Updated:   2025-11-19
Version:        1.0
Description:
Text is obtained from a PDF file by using the pdf2image (with poppler) and easyocr libraries.
The PDF file can contain flat text and pictures, RECOMMENDED FOR SCANNED PDFs.
All text is saved in "output_path".
Dependencies:   pdf2image==1.17.0, easyocr==1.7.2, pillow==12.0.0, numpy==2.2.6,
poppler-25.07.0 installed.
"""

from pdf2image import convert_from_path
import easyocr
import numpy as np

pdf_path = "./data/raw/scanned.pdf"
output_path = "./pdf2image_poppler_easyocr_text.txt"

# Create OCR reader
reader = easyocr.Reader(['es', 'en'])   # idiomas que necesites

# Convert PDF to images (for Windows)
# imagenes = convert_from_path(pdf_path, dpi=200, poppler_path=r"/usr/bin/poppler")

# Convert PDF to images (for Linux)
imagenes = convert_from_path(pdf_path, dpi=200)

# 150–300 dpi recommended

with open(output_path, "w", encoding="utf-8") as salida:

    # Process every page
    for i, img in enumerate(imagenes, start=1):

        # Convert PIL Image → NumPy for EasyOCR
        img_np = np.array(img)

        # Perform OCR
        texto = reader.readtext(img_np, detail=0)  # detail=0: solo texto

        # Save the file
        salida.write(f"\n--- Página {i} ---\n")
        for linea in texto:
            salida.write(linea + "\n")

print(f"Text saved in {output_path}")
