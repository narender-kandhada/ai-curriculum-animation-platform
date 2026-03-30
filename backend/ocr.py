import pytesseract
from PIL import Image

# If Tesseract is not in PATH, set path explicitly (Windows common location):
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path: str) -> str:
    """Extract text from an image file using Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
