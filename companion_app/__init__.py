# Mark the directory as a Python package
from .exercises import get_relaxation_exercise, get_exercise_duration  # Import from submodules
from .ui import display_game_elements, display_relaxation_instructions  # Import from submodules

__all__ = [
    "exercises",
    "ui",
    "get_relaxation_exercise",
    "get_exercise_duration",
    "display_game_elements",
    "display_relaxation_instructions",
]  # Explicitly export required elements