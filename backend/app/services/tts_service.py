from gtts import gTTS

class TTSService:
    def generate_audio(self, text):
        file = "output.mp3"
        tts = gTTS(text)
        tts.save(file)
        return f"Audio saved as {file}"pip
from gtts import gTTS

tts = gTTS(script)
tts.save("story.mp3")

print("🎤 Audio created")