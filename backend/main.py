from fastapi import FastAPI, UploadFile, File
import shutil
from ocr import extract_text
from ai import generate_script

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text("temp.jpg")
    clean_text = text.replace("\n", " ").strip()

    # Generate script
    script = generate_script(clean_text)

    return {
        "text": clean_text,
        "script": script
    }