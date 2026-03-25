"""
Tokenizer utilities for model inputs
"""


class Tokenizer:
    """Text tokenizer wrapper"""
    
    def __init__(self, model_name: str):
        self.model_name = model_name
    
    def encode(self, text: str) -> list:
        """Encode text to token ids"""
        pass
    
    def decode(self, token_ids: list) -> str:
        """Decode token ids to text"""
        pass
