#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           ocr_executable_linux.py
Author:         Antonio Arteaga
Last Updated:   2025-11-19
Version:        1.0
Description:
Simple example of converting to executable a script that uses poppler,
easyocr and tesseract models  (for Linux).
Dependencies:   pdf2image==1.17.0, easyocr==1.7.2, pillow==12.0.0, numpy==2.2.6,
poppler-25.07.0 and tesseractOCR installed.
Instructions for portability:
1. Tesseract and Poppler are expected to be installed on the system, else run:
$ sudo apt-get install tesseract-ocr tesseract-ocr-spa tesseract-ocr-eng
$ sudo apt-get install poppler-utils
2. Copy content of (hidden folder) r'~/.EasyOCR/model' in './easyOCR'.
3. Run (2 lines are 1 line):
pyinstaller --onefile --add-data "easyOCR;easyOCR" --add-data "data;data"
ocr_executable_linux.py
Finally, your executable is created in './dist'
"""
import sys
import os
from pathlib import Path
import numpy as np
from PIL import Image
from pdf2image import convert_from_path
import easyocr
import pytesseract as tess

# Base path (normal script or executable)
if getattr(sys, "frozen", False):
    BASE_PATH = Path(sys._MEIPASS)
else:
    BASE_PATH = Path(__file__).resolve().parent

PDF_PATH = BASE_PATH / "data" / "raw" / "vectorized_simple.pdf"
IMG_PATH = BASE_PATH / "data" / "raw" / "example1.png"

# EasyOCR models path
EASYOCR_MODELS = BASE_PATH / "easyOCR"

reader = easyocr.Reader(
    ['es', 'en'],
    model_storage_directory=str(EASYOCR_MODELS),
    download_enabled=False
)


def process_pdf(pdf_file: Path):
    print("\n=== PROCESSING PDF WITH EASYOCR ===\n")

    images = convert_from_path(str(pdf_file), dpi=200)

    for idx, img in enumerate(images, start=1):
        print(f"\n--- Page {idx} ---\n")
        result = reader.readtext(np.array(img), detail=0)
        print(result[:10], "...")


def process_image(img_file: Path):
    print("\n=== IMAGE PROCESSING WITH TESSERACT ===\n")
    img = Image.open(img_file)
    text = tess.image_to_string(img, lang='eng')
    print(text)


def main():
    process_pdf(PDF_PATH)
    process_image(IMG_PATH)


if __name__ == "__main__":
    main()
