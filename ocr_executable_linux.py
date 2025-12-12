
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path
import numpy as np
from PIL import Image
from pdf2image import convert_from_path
import easyocr
import pytesseract as tess
''' Tesseract and Poppler are expected to be installed on the system.
$ sudo apt-get install tesseract-ocr tesseract-ocr-spa tesseract-ocr-eng
$ sudo apt-get install poppler-utils
'''
# ------------------------------------------------------------
# CONFIGURACIÓN DE RUTAS BASE
# ------------------------------------------------------------
if getattr(sys, "frozen", False):
    # Modo ejecutable (.bin de PyInstaller)
    BASE_PATH = Path(sys._MEIPASS)
else:
    # Modo script normal
    BASE_PATH = Path(__file__).resolve().parent


# ------------------------------------------------------------
# RUTAS DE ARCHIVOS (ya incluidas en tu proyecto)
# ------------------------------------------------------------
PDF_PATH = BASE_PATH / "data" / "raw" / "vectorized_simple.pdf"
IMG_PATH = BASE_PATH / "data" / "raw" / "example1.png"

# ------------------------------------------------------------
# EASYOCR (modelos empacados dentro del proyecto)
# ------------------------------------------------------------
EASYOCR_MODELS = BASE_PATH / "easyOCR"

reader = easyocr.Reader(
    ['es', 'en'],
    model_storage_directory=str(EASYOCR_MODELS),
    download_enabled=False
)

# ------------------------------------------------------------
# POPPLER (en Linux no requiere incluir binarios)
# ------------------------------------------------------------
# convert_from_path() usará poppler del sistema
# Instalar en Ubuntu/Debian:
# sudo apt install poppler-utils

# ------------------------------------------------------------
# TESSERACT OCR (se usa el binario del sistema)
# ------------------------------------------------------------
# Instalar en Ubuntu/Debian:
# sudo apt install tesseract-ocr tesseract-ocr-spa tesseract-ocr-eng
# ------------------------------------------------------------


def process_pdf(pdf_file: Path):
    print("\n=== PROCESANDO PDF CON EASYOCR ===\n")

    images = convert_from_path(str(pdf_file), dpi=200)

    for idx, img in enumerate(images, start=1):
        print(f"\n--- Página {idx} ---\n")
        result = reader.readtext(np.array(img), detail=0)
        print(result[:10], "...")


def process_image(img_file: Path):
    print("\n=== PROCESANDO IMAGEN CON TESSERACT ===\n")
    img = Image.open(img_file)
    text = tess.image_to_string(img, lang='eng')
    print(text)


def main():
    process_pdf(PDF_PATH)
    process_image(IMG_PATH)


if __name__ == "__main__":
    main()
