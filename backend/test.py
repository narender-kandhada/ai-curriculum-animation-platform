import pytesseract
from PIL import Image

# 👉 Set correct Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 👉 Open image
img = Image.open("image.jpg")   # make sure image is in same folder

# 👉 Extract text
text = pytesseract.image_to_string(img)

# 👉 Clean text (IMPORTANT)
clean_text = text.replace("\n", " ").replace("|", "I").strip()

# 👉 Print output
print("===== RAW TEXT =====")
print(text)

print("\n===== CLEAN TEXT =====")
print(clean_text)
from ai import generate_script

print("\n===== GENERATING SCRIPT =====\n")

script = generate_script(clean_text)

print(script)
from db import save_data

save_data(clean_text, script)

print("✅ Saved to DB")