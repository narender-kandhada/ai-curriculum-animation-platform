# 🎓 AI Curriculum to Animation Platform

## 🚀 Overview

An AI-powered learning platform that transforms textbook content into **interactive explanations, animations, and voice narration** in English and Telugu.
The system bridges the gap between static learning and engaging, visual education.

---

## 🎯 Problem Statement

Traditional learning methods rely heavily on textbooks and static content, making it difficult for students to understand complex concepts.
This project aims to automate the conversion of curriculum content into **visual and audio learning experiences** using AI.

---

## 🧠 Key Features

* 📚 Generate **simple explanations** from topics or uploaded images
* 🔍 Extract text from curriculum images using **OCR (Tesseract)**
* 🤖 Generate animation scripts using **Groq LLaMA 3.3 70B**
* 🎥 Convert concepts into **visual animations**
* 🔊 Provide **voice narration (gTTS)**
* 💾 Store results in **MongoDB**
* ⚡ Interactive **web-based interface**
* 🔄 Scalable for multiple subjects

---

## 🏗️ Project Architecture

```
User Input (Frontend)
        ↓
Backend (FastAPI)
        ↓
OCR (Tesseract) ──→ Text Extraction
        ↓
AI Model (Groq / LLaMA 3.3 70B) ──→ Script Generation
        ↓
Animation Engine ──→ Scene Descriptions
        ↓
TTS (gTTS) ──→ Audio Narration
        ↓
MongoDB ──→ Save Results
        ↓
Frontend Output (Text + Animation + Audio)
```

---

## 🛠️ Tech Stack

| Layer       | Technology                              |
|------------|------------------------------------------|
| Frontend   | React (Vite)                             |
| Backend    | FastAPI (Python 3.11)                    |
| LLM        | Groq — LLaMA 3.3 70B Versatile           |
| OCR        | Tesseract via `pytesseract`              |
| Animation  | Python AnimationService / Manim (planned)|
| TTS        | gTTS (Google Text-to-Speech)             |
| Database   | MongoDB via `pymongo`                    |
| Deployment | Docker + Vercel + Render                 |

---

## 📁 Project Structure

```
ai-curriculum-animation-platform/
│
├── backend/           # FastAPI server (see backend/README.md)
│   ├── app/           # App modules (routes, services, schemas, core)
│   ├── main.py        # OCR + script pipeline entry point
│   ├── ai.py          # Groq LLM client
│   ├── ocr.py         # Tesseract OCR
│   ├── db.py          # MongoDB connection
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env           # (not committed — add your own)
│
├── frontend/          # React UI (Vite)
├── animation/         # Animation engine
├── tts/               # Voice generation
├── model/             # AI/ML components
├── data/              # Dataset processing
├── shared/            # Prompts & schemas
├── tests/             # Test suite
└── docker-compose.yml
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/narender-kandhada/ai-curriculum-animation-platform.git
cd ai-curriculum-animation-platform
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file inside `backend/`:

```env
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=mongodb://localhost:27017/
```

Start the server:

```bash
uvicorn app.main:app --reload
```

> 📖 See [backend/README.md](./backend/README.md) for full backend documentation.

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

### 4️⃣ Run with Docker (Optional)

```bash
docker-compose up --build
```

---

## 🔌 API Endpoints

| Method | Endpoint        | Description                              |
|--------|----------------|------------------------------------------|
| GET    | `/`            | Health check                             |
| POST   | `/upload/`     | Upload image → OCR → generate script     |
| POST   | `/api/generate`| Text prompt → script + animation + audio |

### Example — `POST /api/generate`

**Request:**
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

## 👥 Team Roles

* 🧠 AI/ML Lead — Model & prompts
* 📊 Data Engineer — Dataset processing
* 🔧 Backend Developer — API & integration
* 🎨 Frontend Developer — UI/UX
* 🎥 Animation + TTS — Visuals & voice

---

## 📅 Timeline (30 Days)

* **Week 1:** Dataset + Setup ✅
* **Week 2:** Model integration (Groq / LLaMA) ✅
* **Week 3:** Backend + Animation + TTS 🔄
* **Week 4:** Frontend + Deployment ⏳

---

## ⚠️ Project Scope Strategy

✔ Focus on **3–5 topics working perfectly**  
✔ Build **end-to-end pipeline**  
❌ Avoid over-complex features early  

---

## 🌟 Future Improvements

* Full offline model (no API dependency)
* Better animation engine (Manim integration)
* Multi-language support (Telugu, Hindi)
* Personalized learning paths
* Real-time streaming responses

---

## 📌 Demo Flow

1. Upload a curriculum image or enter a topic
2. Backend extracts text via OCR
3. LLM generates an animation script
4. Animation engine creates scene descriptions
5. gTTS generates audio narration
6. Results saved to MongoDB
7. Frontend displays explanation + animation + audio player

---

## 🤝 Contribution

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

This project is for educational purposes.

---

## 💡 Acknowledgment

Built as part of an AI/ML academic project to enhance student learning using modern AI technologies.

---
