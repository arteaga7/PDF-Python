# PDF-Python
This repository contains some scripts using Python libraries to process PDF files and images.

## 🚀 How to run locally
1. Clone this repository:
```
git clone https://github.com/arteaga7/PDF-OCR-Python.git
```
2. Set virtual environment and install dependencies.

For Windows:
```
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
```
For Linux:
```
python -m venv env && source env/bin/activate && pip install -r requirements.txt
```
3. Run any Python script.

## 📦 Make any Python script executable
In order to make 'ocr_executable_windows.py' executable (for Windows):
1. Copy the content of 'C:/poppler/Library' in the folder './poppler'.
2. Copy content of (hidden folder) 'C:/Users/youruser/.EasyOCR/model' in './easyOCR'.
3. Copy the content of 'C:/Program Files/Tesseract-OCR' in './tesseract'.
4. The project structure should be:
```
executable_project/
│
├── ocr_executable_windows.py
├── .gitignore
├── env/                # Virtual enviroment
└── requirements.txt
└── data/               # Contains all source files (PDFs, etc.)
        └── raw/        # Non-processed files
        └── ...
└── easyOCR/            # Contains easyOCR models (not provided and used for executable)
        └── *.pth       # Models
└── poppler/            # Contains poppler files (not provided and used for executable)
        └── bin/        # Binary files
        └── ...
└── tesseract/          # Contains tesseract models (not provided and used for executable)
        └── tessdata/
        └── tesseract.exe
        └── ...
```
5. Run:
```
pyinstaller --onefile --add-data "poppler/bin;poppler/bin" --add-data "easyOCR;easyOCR" --add-data "tesseract;tesseract" --add-data "data;data" ocr_executable_windows.py
```
6. Paste/move folder './data', which contains the PDF files, in the same path of your executable.exe created in './dist'.

In order to make 'ocr_executable_linux.py' executable (for Linux):
1. Tesseract and Poppler are expected to be installed on the system, else run:
```
sudo apt-get install tesseract-ocr tesseract-ocr-spa tesseract-ocr-eng
```
```
sudo apt-get install poppler-utils
```
2. Copy content of (hidden folder) '~/.EasyOCR/model' in './easyOCR'.
3. Run:
```
pyinstaller --onefile --add-data "easyOCR;easyOCR" --add-data "data;data" ocr_executable_linux.py
```
Finally, your executable is created in './dist'.
