"""
Text-to-speech service
"""


class TTSService:
    """Service for text-to-speech synthesis"""
    
    def __init__(self):
        self.engine = None
    
    def synthesize(self, text: str, voice: str = "default") -> bytes:
        """Convert text to speech audio"""
        pass
    
    def get_available_voices(self) -> list:
        """Get list of available voices"""
        pass
