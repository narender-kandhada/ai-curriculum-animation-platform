from fastapi import APIRouter
from pydantic import BaseModel

from services.model_service import ModelService
from services.animation_service import AnimationService
from services.tts_service import TTSService

router = APIRouter(prefix="/api")

# request schema
class GenerationRequest(BaseModel):
    prompt: str
    parameters: dict = {}

# services
model_service = ModelService()
animation_service = AnimationService()
tts_service = TTSService()

@router.post("/generate")
async def generate_content(request: GenerationRequest):

    # AI
    result = await model_service.generate(request.prompt)

    # animation
    animation = animation_service.create_animation(result)

    # audio
    audio = tts_service.generate_audio(result)

    # save output
    with open("output.txt", "w") as f:
        f.write(result)

    return {
        "text": result,
        "animation": animation,
        "audio": audio
    }