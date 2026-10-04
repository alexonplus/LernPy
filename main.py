from engine import GameEngine
from content import PUZZLES

if __name__ == "__main__":
    game = GameEngine(PUZZLES)
    try:
        game.run()
    except KeyboardInterrupt:
        print("\nИгра прервана. До встречи!")
