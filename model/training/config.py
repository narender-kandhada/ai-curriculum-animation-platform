"""
Training configuration
"""

from dataclasses import dataclass


@dataclass
class TrainingConfig:
    """Configuration for model training"""
    learning_rate: float = 2e-4
    batch_size: int = 4
    num_epochs: int = 3
    max_seq_length: int = 512
    output_dir: str = "./outputs/models"
