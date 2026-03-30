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
├── ai.py                     # Groq LLM client & generate_script() — loads key from .env
├── ocr.py                    # Tesseract OCR — extract_text()
├── db.py                     # MongoDB connection — loads URI from .env
├── key.py                    # Legacy upload route (OCR → script)
├── test.py                   # Manual test scripts
├── Dockerfile                # Docker image definition
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed to git)
└── README.md                 # You are here
```

---

## ⚙️ Tech Stack

| Layer        | Technology                                           |
|-------------|-------------------------------------------------------|
| Framework   | [FastAPI](https://fastapi.tiangolo.com/)              |
| LLM         | [Groq](https://groq.com/) — LLaMA 3.3 70B Versatile  |
| OCR         | [Tesseract](https://github.com/tesseract-ocr/tesseract) via `pytesseract` |
| TTS         | [gTTS](https://gtts.readthedocs.io/) (Google Text-to-Speech) |
| Database    | [MongoDB](https://www.mongodb.com/) via `pymongo`     |
| Validation  | [Pydantic v2](https://docs.pydantic.dev/)             |
| Server      | [Uvicorn](https://www.uvicorn.org/) (ASGI)            |
| Container   | Docker (Python 3.11 slim)                             |

---

## 🚀 Getting Started

### 1. Clone & enter the backend directory

```bash
git clone https://github.com/narender-kandhada/ai-curriculum-animation-platform.git
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

> **Note:** `torch` and `transformers` are large packages (~3–5 GB). Ensure sufficient disk space.

### 4. Configure environment variables

Create a `.env` file in the `backend/` directory (already in `.gitignore`):

```env
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=mongodb://localhost:27017/
```

- Get your free Groq API key at [console.groq.com](https://console.groq.com)
- Install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) (Windows) and ensure it's in your `PATH`

### 5. Run the development server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API: **http://localhost:8000**  
- Interactive docs: **http://localhost:8000/docs**

---

## 🐳 Docker

### Build the image

```bash
docker build -t ai-curriculum-backend .
```

### Run the container

```bash
docker run --env-file .env -p 8000:8000 ai-curriculum-backend
```

---

## 📡 API Endpoints

### `GET /`
Health check.

**Response:**
```json
{ "message": "Hello Bro 🚀" }
```

---

### `POST /upload/`
Upload an image — extracts text via OCR and generates an animation script.

**Request:** `multipart/form-data` with field `file` (image).

**Response:**
```json
{
  "text": "<extracted text from image>",
  "script": "<LLM-generated animation script>"
}
```

---

### `POST /api/generate`
Send a text prompt to trigger the full AI pipeline (LLM → Animation → TTS).

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

```bash
python test.py
```

Or use the Swagger UI at `http://localhost:8000/docs`.

---

## 🔑 Environment Variables

| Variable        | Description                        | Default                        |
|----------------|------------------------------------|--------------------------------|
| `GROQ_API_KEY` | Groq LLM API key                   | *(required)*                   |
| `MONGO_URI`    | MongoDB connection string          | `mongodb://localhost:27017/`   |

> ⚠️ Never commit `.env` to version control. It is already excluded via `.gitignore`.

---

## 📦 Dependencies

```
fastapi==0.104.1        # Web framework
uvicorn==0.24.0         # ASGI server
pydantic==2.5.0         # Data validation
pydantic-settings==2.1.0
torch==2.1.0            # ML framework
transformers==4.35.0    # HuggingFace models
peft==0.7.0             # Parameter-efficient fine-tuning
pytesseract             # OCR wrapper
Pillow                  # Image processing
groq                    # Groq LLM client
python-multipart        # File upload support
python-dotenv           # Load .env variables
pymongo                 # MongoDB driver
gtts                    # Google Text-to-Speech
```

---

## 🛠️ Development Notes

- CORS is set to `allow_origins=["*"]` — **restrict this in production**
- `output.txt` and `output.mp3` are written to the working directory on each generation
- Tesseract must be installed separately: [Windows installer](https://github.com/UB-Mannheim/tesseract/wiki)
- MongoDB must be running locally or provide a cloud URI (e.g., MongoDB Atlas)

---

## 📄 License

Part of the **AI Curriculum Animation Platform**. See root-level `LICENSE` for details.
