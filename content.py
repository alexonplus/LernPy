from models import Puzzle, Difficulty, Language

PUZZLES = {
    Language.RU: [
        Puzzle(
            id=1, difficulty=Difficulty.EASY,
            title="Сложение строк и чисел",
            code="print('5' * 3)",
            question="Какой будет результат?",
            options=["15", "555", "Ошибка", "'5' * 3"],
            correct_answer=2,
            explanation="Умножение строки на целое число N повторяет эту строку N раз."
        ),
        Puzzle(
            id=2, difficulty=Difficulty.MEDIUM,
            title="Хитрые списки",
            code="a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            question="Что выведет этот код на экран?",
            options=["[1, 2, 3]", "[1, 2, 3, 4]", "Ошибка", "None"],
            correct_answer=2,
            explanation="Переменные указывают на объекты. `a` и `b` ссылаются на один и тот же список в памяти."
        ),
        Puzzle(
            id=3, difficulty=Difficulty.HARD,
            title="Замыкания и циклы",
            code="funcs = []\nfor i in range(3):\n    funcs.append(lambda: i)\n\nfor f in funcs:\n    print(f(), end=' ')",
            question="Что выведет этот код?",
            options=["0 1 2", "2 2 2", "1 2 3", "Ошибка"],
            correct_answer=2,
            explanation="Лямбда-функции захватывают переменную `i` по ссылке (позднее связывание)."
        ),
        Puzzle(
            id=4, difficulty=Difficulty.HARD,
            title="Изменяемые аргументы по умолчанию",
            code="def add_item(item, items=[]):\n    items.append(item)\n    return items\n\nprint(add_item(1))\nprint(add_item(2))",
            question="Что выведет второй вызов функции?",
            options=["[2]", "[1, 2]", "Ошибка", "None"],
            correct_answer=2,
            explanation="Значения по умолчанию вычисляются один раз при определении функции."
        )
    ],
    Language.EN: [
        Puzzle(
            id=1, difficulty=Difficulty.EASY,
            title="String and Integer Multiplication",
            code="print('5' * 3)",
            question="What will be the output?",
            options=["15", "555", "Error", "'5' * 3"],
            correct_answer=2,
            explanation="Multiplying a string by an integer N repeats the string N times."
        ),
        Puzzle(
            id=2, difficulty=Difficulty.MEDIUM,
            title="Tricky Lists",
            code="a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            question="What will this code print?",
            options=["[1, 2, 3]", "[1, 2, 3, 4]", "Error", "None"],
            correct_answer=2,
            explanation="Variables are references. `a` and `b` point to the same list in memory."
        ),
        Puzzle(
            id=3, difficulty=Difficulty.HARD,
            title="Closures and Loops",
            code="funcs = []\nfor i in range(3):\n    funcs.append(lambda: i)\n\nfor f in funcs:\n    print(f(), end=' ')",
            question="What will this code output?",
            options=["0 1 2", "2 2 2", "1 2 3", "Error"],
            correct_answer=2,
            explanation="Lambda functions capture the variable `i` by reference (late binding)."
        ),
        Puzzle(
            id=4, difficulty=Difficulty.HARD,
            title="Mutable Default Arguments",
            code="def add_item(item, items=[]):\n    items.append(item)\n    return items\n\nprint(add_item(1))\nprint(add_item(2))",
            question="What will the second function call print?",
            options=["[2]", "[1, 2]", "Error", "None"],
            correct_answer=2,
            explanation="Default values are evaluated only once at function definition time."
        )
    ]
}
