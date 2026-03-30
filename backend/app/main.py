from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.generate import router as generate_router

app = FastAPI(title="AI Curriculum Animation Platform")

# CORS (simple)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include route
app.include_router(generate_router)

@app.get("/")
def home():
    return {"message": "Hello Bro 🚀"}