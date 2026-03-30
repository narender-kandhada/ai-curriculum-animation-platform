# 🎓 AI Curriculum Animation Platform — Backend

A **FastAPI**-powered backend that takes educational content (images/text), extracts information via OCR, generates animation scripts using an LLM (Groq / LLaMA 3.3), synthesizes narration audio via TTS, and returns structured outputs for frontend consumption.

---

## 📁 Project Structure

```
backend/
├── app/
│   ├── main.py               # FastAPI app factory, CORS, router registration
│   ├── routes/
│   │   ├── _init_.py
│   │   └── generate.py       # POST /api/generate — main generation endpoint
│   ├── services/
│   │   ├── animation_service.py  # AnimationService — creates animation descriptions
│   │   ├── tts_service.py        # TTSService — text-to-speech via gTTS
│   │   └── model_service.py      # ModelService — LLM inference (Groq/LLaMA)
│   ├── schemas/              # Pydantic request/response schemas
│   ├── core/                 # Config, settings, constants
│   └── utils/                # Utility helpers
├── main.py                   # Root entry: OCR + script generation pipeline
├── ai.py                     # Groq LLM client & generate_script()
├── ocr.py                    # Tesseract OCR — extract_text()
├── db.py                     # Database connection setup
├── key.py                    # API key / secrets loader
├── test.py                   # Manual test scripts
├── Dockerfile                # Docker image definition
├── requirements.txt          # Python dependencies
└── README.md                 # You are here
```

---

## ⚙️ Tech Stack

| Layer        | Technology                              |
|-------------|------------------------------------------|
| Framework   | [FastAPI](https://fastapi.tiangolo.com/) |
| LLM         | [Groq](https://groq.com/) — LLaMA 3.3 70B Versatile |
| OCR         | [Tesseract](https://github.com/tesseract-ocr/tesseract) via `pytesseract` |
| TTS         | [gTTS](https://gtts.readthedocs.io/) (Google Text-to-Speech) |
| Validation  | [Pydantic v2](https://docs.pydantic.dev/) |
| Server      | [Uvicorn](https://www.uvicorn.org/) (ASGI) |
| Container   | Docker (Python 3.11 slim) |

---

## 🚀 Getting Started

### 1. Clone & enter the backend directory

```bash
git clone <repo-url>
cd ai-curriculum-animation-platform/backend
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `torch` and `transformers` are large packages. Ensure you have enough disk space (~3–5 GB).

### 4. Configure environment / API keys

- Set your **Groq API key** in `key.py` or via an environment variable `GROQ_API_KEY`.
- Ensure [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) is installed on your system and available in `PATH`.

### 5. Run the development server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: **http://localhost:8000**

Interactive API docs: **http://localhost:8000/docs**

---

## 🐳 Docker

### Build the image

```bash
docker build -t ai-curriculum-backend .
```

### Run the container

```bash
docker run -p 8000:8000 ai-curriculum-backend
```

---

## 📡 API Endpoints

### `GET /`
Health check endpoint.

**Response:**
```json
{ "message": "Hello Bro 🚀" }
```

---

### `POST /upload/`
Upload an image file; the backend extracts text via OCR and generates an animation script.

**Request:** `multipart/form-data` with a field `file` (image).

**Response:**
```json
{
  "text": "<extracted text from image>",
  "script": "<LLM-generated animation script>"
}
```

---

### `POST /api/generate`
Send a text prompt directly to trigger the full generation pipeline (LLM → Animation → TTS).

**Request body:**
```json
{
  "prompt": "Explain photosynthesis for kids",
  "parameters": {}
}
```

**Response:**
```json
{
  "text": "<generated script>",
  "animation": "<animation description>",
  "audio": "Audio saved as output.mp3"
}
```

---

## 🧪 Testing

Run the manual test script:

```bash
python test.py
```

Or use the interactive Swagger UI at `http://localhost:8000/docs`.

---

## 🔑 Environment Variables

| Variable        | Description                          | Default      |
|----------------|--------------------------------------|--------------|
| `GROQ_API_KEY` | API key for Groq LLM service         | *(required)* |
| `HOST`         | Server bind address                  | `0.0.0.0`    |
| `PORT`         | Server port                          | `8000`       |

> ⚠️ **Security Warning:** Do not hardcode API keys in source files. Use `.env` files or environment variables and add them to `.gitignore`.

---

## 📦 Key Dependencies

```
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0
torch==2.1.0
transformers==4.35.0
peft==0.7.0
pytesseract
Pillow
groq
python-multipart
gtts
```

---

## 🛠️ Development Notes

- CORS is currently set to `allow_origins=["*"]` — **restrict this in production**.
- The `output.txt` and `output.mp3` files are written to the working directory on each generation request.
- Tesseract must be installed separately from pip. Download it from [here](https://github.com/UB-Mannheim/tesseract/wiki) (Windows) or via your system package manager.

---

## 📄 License

This project is part of the **AI Curriculum Animation Platform**. See the root-level `LICENSE` file for details.
