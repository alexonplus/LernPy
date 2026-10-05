from enum import Enum
from dataclasses import dataclass
from typing import List

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Language(Enum):
    RU = "ru"
    EN = "en"

class PuzzleType(Enum):
    OUTPUT = "output"
    BUG = "bug"

@dataclass
class Puzzle:
    id: int
    difficulty: Difficulty
    type: PuzzleType
    title: str
    code: str
    question: str
    options: List[str]
    correct_answer: int
    explanation: str
