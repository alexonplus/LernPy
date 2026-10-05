from models import Puzzle, Difficulty, Language, PuzzleType

PUZZLES = {
    Language.RU: [
        Puzzle(
            id=1, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="Сложение строк и чисел",
            code="print('5' * 3)",
            question="Какой будет результат?",
            options=["15", "555", "Ошибка", "'5' * 3"],
            correct_answer=2,
            explanation="Умножение строки на целое число N повторяет эту строку N раз."
        ),
        Puzzle(
            id=2, difficulty=Difficulty.EASY, type=PuzzleType.BUG,
            title="Проблема с отступами",
            code="1| def is_even(num):\n2|     if num % 2 == 0:\n3|     return True\n4|     else:\n5|         return False",
            question="Код выдает ошибку IndentationError. В какой строке запрятан баг?",
            options=["Строка 2", "Строка 3", "Строка 4", "Строка 5"],
            correct_answer=2,
            explanation="В Python отступы определяют блоки кода. `return True` в строке 3 должен быть сдвинут вправо (внутрь `if`)."
        ),
        Puzzle(
            id=3, difficulty=Difficulty.MEDIUM, type=PuzzleType.OUTPUT,
            title="Хитрые списки",
            code="a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            question="Что выведет этот код на экран?",
            options=["[1, 2, 3]", "[1, 2, 3, 4]", "Ошибка", "None"],
            correct_answer=2,
            explanation="Переменные указывают на объекты. `a` и `b` ссылаются на один и тот же список в памяти."
        ),
        Puzzle(
            id=4, difficulty=Difficulty.MEDIUM, type=PuzzleType.BUG,
            title="Опасные значения по умолчанию",
            code="1| def add_item(item, items=[]):\n2|     items.append(item)\n3|     return items\n4| \n5| print(add_item(1))\n6| print(add_item(2))",
            question="Функция сохраняет данные между вызовами, а не создает новый список. В какой строке баг?",
            options=["Строка 1", "Строка 2", "Строка 3", "Строка 5"],
            correct_answer=1,
            explanation="Изменяемые аргументы по умолчанию (`items=[]`) вычисляются один раз при создании функции. Нужно использовать `items=None`."
        ),
        Puzzle(
            id=5, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Замыкания и циклы",
            code="funcs = []\nfor i in range(3):\n    funcs.append(lambda: i)\n\nfor f in funcs:\n    print(f(), end=' ')",
            question="Что выведет этот код?",
            options=["0 1 2", "2 2 2", "1 2 3", "Ошибка"],
            correct_answer=2,
            explanation="Лямбда-функции захватывают переменную `i` по ссылке (позднее связывание)."
        )
    ],
    Language.EN: [
        Puzzle(
            id=1, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="String and Integer Multiplication",
            code="print('5' * 3)",
            question="What will be the output?",
            options=["15", "555", "Error", "'5' * 3"],
            correct_answer=2,
            explanation="Multiplying a string by an integer N repeats the string N times."
        ),
        Puzzle(
            id=2, difficulty=Difficulty.EASY, type=PuzzleType.BUG,
            title="Indentation Problem",
            code="1| def is_even(num):\n2|     if num % 2 == 0:\n3|     return True\n4|     else:\n5|         return False",
            question="The code throws an IndentationError. Which line contains the bug?",
            options=["Line 2", "Line 3", "Line 4", "Line 5"],
            correct_answer=2,
            explanation="In Python, indentation defines code blocks. `return True` on line 3 must be indented further inside the `if`."
        ),
        Puzzle(
            id=3, difficulty=Difficulty.MEDIUM, type=PuzzleType.OUTPUT,
            title="Tricky Lists",
            code="a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            question="What will this code print?",
            options=["[1, 2, 3]", "[1, 2, 3, 4]", "Error", "None"],
            correct_answer=2,
            explanation="Variables are references. `a` and `b` point to the same list in memory."
        ),
        Puzzle(
            id=4, difficulty=Difficulty.MEDIUM, type=PuzzleType.BUG,
            title="Dangerous Default Values",
            code="1| def add_item(item, items=[]):\n2|     items.append(item)\n3|     return items\n4| \n5| print(add_item(1))\n6| print(add_item(2))",
            question="The function persists data across calls instead of creating a new list. Which line is the bug?",
            options=["Line 1", "Line 2", "Line 3", "Line 5"],
            correct_answer=1,
            explanation="Mutable default arguments (`items=[]`) are evaluated only once at definition time. You should use `items=None`."
        ),
        Puzzle(
            id=5, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Closures and Loops",
            code="funcs = []\nfor i in range(3):\n    funcs.append(lambda: i)\n\nfor f in funcs:\n    print(f(), end=' ')",
            question="What will this code output?",
            options=["0 1 2", "2 2 2", "1 2 3", "Error"],
            correct_answer=2,
            explanation="Lambda functions capture the variable `i` by reference (late binding)."
        )
    ]
}
