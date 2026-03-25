"""
LoRA (Low-Rank Adaptation) configuration
"""

from dataclasses import dataclass


@dataclass
class LoRAConfig:
    """Configuration for LoRA fine-tuning"""
    r: int = 8
    lora_alpha: int = 32
    target_modules: list = None
    lora_dropout: float = 0.1
    bias: str = "none"
    
    def __post_init__(self):
        if self.target_modules is None:
            self.target_modules = ["q_proj", "v_proj"]
