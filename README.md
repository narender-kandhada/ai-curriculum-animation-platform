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

* 📚 Generate **simple explanations** from topics
* 🎥 Convert concepts into **visual animations**
* 🔊 Provide **voice narration (Telugu + English)**
* ⚡ Interactive **web-based interface**
* 🔄 Scalable for multiple subjects

---

## 🏗️ Project Architecture

```
User Input (Frontend)
        ↓
Backend (FastAPI)
        ↓
AI Model (API / Local Model)
        ↓
Animation Engine
        ↓
TTS (Voice Generation)
        ↓
Frontend Output (Text + Video + Audio)
```

---

## 🛠️ Tech Stack

| Layer      | Technology                    |
| ---------- | ----------------------------- |
| Frontend   | React (Vite)                  |
| Backend    | FastAPI (Python)              |
| AI Model   | OpenAI / HuggingFace / Ollama |
| Animation  | Python Templates / Manim      |
| TTS        | gTTS / Coqui                  |
| Deployment | Vercel + Render               |

---

## 📁 Project Structure

```
ai-curriculum-animation-platform/
│
├── data/              # Dataset processing
├── model/             # AI/ML components
├── backend/           # FastAPI server
├── frontend/          # React UI
├── animation/         # Animation engine
├── tts/               # Voice generation
├── shared/            # Prompts & schemas
├── docs/              # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-curriculum-animation-platform.git
cd ai-curriculum-animation-platform
```

---

### 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

### 4️⃣ Run Local Model (Optional)

Using Ollama:

```bash
ollama run phi
```

---

## 🔌 API Endpoint

### POST `/generate`

**Request:**

```json
{
  "topic": "Photosynthesis"
}
```

**Response:**

```json
{
  "explanation": "...",
  "animation_script": "...",
  "audio_url": "...",
  "video_url": "..."
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

* **Week 1:** Dataset + Setup
* **Week 2:** Model training / integration
* **Week 3:** Backend + Animation + TTS
* **Week 4:** Frontend + Deployment 

---

## ⚠️ Project Scope Strategy

✔ Focus on **3–5 topics working perfectly**
✔ Build **end-to-end pipeline**
❌ Avoid over-complex features early

---

## 🌟 Future Improvements

* Full offline model (no API dependency)
* Better animation engine
* Multi-language support
* Personalized learning paths

---

## 📌 Demo Flow

1. Enter a topic
2. Click "Generate"
3. View explanation
4. Watch animation
5. Listen to narration

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
