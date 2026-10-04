# LernPy 🐍

LernPy is an interactive, gamified terminal application designed to teach Python through tricky puzzles and non-obvious code examples. 

Instead of boring theoretical lectures, LernPy challenges you to predict the output of Python snippets right in your terminal. It features a beautiful CLI interface built with the [Rich](https://github.com/Textualize/rich) library.

## Features
- **Interactive Puzzles:** Guess the output of code involving closures, mutable defaults, reference assignments, and more.
- **Beautiful Terminal UI:** Syntax highlighting, colored text, and formatted panels.
- **Educational Explanations:** Every puzzle comes with a detailed explanation of *why* Python behaves the way it does.

## How to Run

1. Make sure you have Python installed.
2. Clone this repository.
3. Run the application:
   - **On Windows:** Just run `run.bat` in your terminal.
   - **On Linux/Mac:** 
     ```bash
     python -m venv venv
     source venv/bin/activate
     pip install rich
     python main.py
     ```

## Customization
You can easily add new puzzles by editing the `PUZZLES` list in the `content.py` file!

---
*Created as a fun way to explore the tricky parts of Python.*
