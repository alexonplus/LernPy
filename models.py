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

@dataclass
class Puzzle:
    id: int
    difficulty: Difficulty
    title: str
    code: str
    question: str
    options: List[str]
    correct_answer: int
    explanation: str
