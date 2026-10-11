from models import Puzzle, Difficulty, Language, PuzzleType

PUZZLES = {
    Language.RU: [
        # --- EASY ---
        Puzzle(
            id=1, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="Сложение строк и чисел",
            code="print('5' * 3)",
            question="Какой будет результат выполнения?",
            options=["15", "555", "Ошибка TypeError", "'5' * 3"],
            correct_answer=2,
            explanation="Умножение строки на целое число N повторяет эту строку N раз ('5' * 3 = '555')."
        ),
        Puzzle(
            id=2, difficulty=Difficulty.EASY, type=PuzzleType.BUG,
            title="Проблема с отступами",
            code="1| def is_even(num):\n2|     if num % 2 == 0:\n3|     return True\n4|     else:\n5|         return False",
            question="Код выдает ошибку IndentationError. В какой строке запрятан баг?",
            options=["Строка 2", "Строка 3", "Строка 4", "Строка 5"],
            correct_answer=2,
            explanation="В Python отступы определяют блоки кода. `return True` в строке 3 должен быть сдвинут вправо (внутрь блока `if`)."
        ),
        Puzzle(
            id=3, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="Истинность коллекций",
            code="print(bool([]), bool([0]))",
            question="Что выведет этот код?",
            options=["True True", "False False", "False True", "True False"],
            correct_answer=3,
            explanation="Пустые коллекции (списки, строки, словари) приводятся к False. Непустой список `[0]` приводится к True, даже если внутри 0."
        ),
        Puzzle(
            id=4, difficulty=Difficulty.EASY, type=PuzzleType.BUG,
            title="Забытое двоеточие",
            code="1| def greet(name)\n2|     message = f'Привет, {name}!'\n3|     return message\n4| \n5| print(greet('Алекс'))",
            question="Код вызывает SyntaxError. В какой строке ошибка?",
            options=["Строка 1", "Строка 2", "Строка 3", "Строка 5"],
            correct_answer=1,
            explanation="В определении функции `def greet(name)` в конце строки пропущено двоеточие `:`."
        ),
        Puzzle(
            id=5, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="Деление в Python 3",
            code="print(type(5 / 2))",
            question="Какой тип данных вернет деление `5 / 2`?",
            options=["<class 'int'>", "<class 'float'>", "<class 'number'>", "<class 'double'>"],
            correct_answer=2,
            explanation="В Python 3 обычный оператор деления `/` всегда возвращает число с плавающей точкой (`float`), даже если результат целый (например, 4 / 2 -> 2.0)."
        ),

        # --- MEDIUM ---
        Puzzle(
            id=6, difficulty=Difficulty.MEDIUM, type=PuzzleType.OUTPUT,
            title="Хитрые списки",
            code="a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            question="Что выведет этот код на экран?",
            options=["[1, 2, 3]", "[1, 2, 3, 4]", "Ошибка", "None"],
            correct_answer=2,
            explanation="Переменные в Python — это ссылки на объекты. `a` и `b` ссылаются на один и тот же список в памяти. Изменение через `b` меняет и `a`."
        ),
        Puzzle(
            id=7, difficulty=Difficulty.MEDIUM, type=PuzzleType.BUG,
            title="Опасные значения по умолчанию",
            code="1| def add_item(item, items=[]):\n2|     items.append(item)\n3|     return items\n4| \n5| print(add_item(1))\n6| print(add_item(2))",
            question="Функция сохраняет данные между вызовами вместо создания нового списка. В какой строке баг?",
            options=["Строка 1", "Строка 2", "Строка 3", "Строка 5"],
            correct_answer=1,
            explanation="Изменяемые аргументы по умолчанию (`items=[]`) вычисляются один раз при создании функции. Следует использовать `items=None`."
        ),
        Puzzle(
            id=8, difficulty=Difficulty.MEDIUM, type=PuzzleType.OUTPUT,
            title="Вложенный поиск в списках",
            code="items = [1, 2, [3, 4]]\nprint(3 in items)",
            question="Что вернет выражение `3 in items`?",
            options=["True", "False", "Ошибка TypeError", "None"],
            correct_answer=2,
            explanation="Оператор `in` проверяет только элементы первого уровня списка. Тройка находится внутри вложенного списка, поэтому результат `False`."
        ),
        Puzzle(
            id=9, difficulty=Difficulty.MEDIUM, type=PuzzleType.BUG,
            title="Неизменяемость строк",
            code="1| greeting = 'hello world'\n2| greeting[0] = 'H'\n3| print(greeting)",
            question="Интерпретатор падает с ошибкой TypeError. В какой строке ошибка?",
            options=["Строка 1", "Строка 2", "Строка 3", "Ошибки нет"],
            correct_answer=2,
            explanation="Строки в Python неизменяемы (immutable). Нельзя переназначить символ по индексу `greeting[0] = 'H'`."
        ),

        # --- HARD ---
        Puzzle(
            id=10, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Замыкания и позднее связывание",
            code="funcs = []\nfor i in range(3):\n    funcs.append(lambda: i)\n\nfor f in funcs:\n    print(f(), end=' ')",
            question="Что выведет этот код?",
            options=["0 1 2", "2 2 2", "1 2 3", "Ошибка NameError"],
            correct_answer=2,
            explanation="Лямбда-функции захватывают переменную `i` по ссылке (позднее связывание). К моменту вызова цикла `i` уже равно 2."
        ),
        Puzzle(
            id=11, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Переопределение в блоке finally",
            code="def compute():\n    try:\n        return 1\n    finally:\n        return 2\n\nprint(compute())",
            question="Что вернет функция `compute()`?",
            options=["1", "2", "Ошибка SyntaxError", "1 2"],
            correct_answer=2,
            explanation="Блок `finally` выполняется всегда перед выходом из функции. Значение `return` в блоке `finally` перезаписывает предыдущий `return 1`."
        ),
        Puzzle(
            id=12, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Коллизия ключей словаря",
            code="data = {1: 'Python', 1.0: 'LernPy', True: 'Awesome'}\nprint(len(data))",
            question="Сколько элементов будет в словаре `data`?",
            options=["3", "2", "1", "Ошибка TypeError"],
            correct_answer=3,
            explanation="В Python `1 == 1.0 == True` и их хэши одинаковы (`hash(1) == hash(1.0) == hash(True)`). Поэтому все три ключа считаются одним и тем же, перезаписывая значение."
        ),
        Puzzle(
            id=13, difficulty=Difficulty.HARD, type=PuzzleType.BUG,
            title="Неизменяемый кортеж",
            code="1| record = (10, 20, [30, 40])\n2| record[2].append(50)\n3| record[0] = 99\n4| print(record)",
            question="В какой строке произойдет ошибка выполнения TypeError?",
            options=["Строка 1", "Строка 2", "Строка 3", "Строка 4"],
            correct_answer=3,
            explanation="Кортеж (tuple) неизменяем. Попытка переназначить его элемент в строке 3 вызовет TypeError. При этом строка 2 легальна, так как меняется сам список внутри кортежа."
        )
    ],
    Language.EN: [
        # --- EASY ---
        Puzzle(
            id=1, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="String and Integer Multiplication",
            code="print('5' * 3)",
            question="What will be the output?",
            options=["15", "555", "TypeError", "'5' * 3"],
            correct_answer=2,
            explanation="Multiplying a string by an integer N repeats the string N times ('5' * 3 = '555')."
        ),
        Puzzle(
            id=2, difficulty=Difficulty.EASY, type=PuzzleType.BUG,
            title="Indentation Problem",
            code="1| def is_even(num):\n2|     if num % 2 == 0:\n3|     return True\n4|     else:\n5|         return False",
            question="The code throws an IndentationError. Which line contains the bug?",
            options=["Line 2", "Line 3", "Line 4", "Line 5"],
            correct_answer=2,
            explanation="In Python, indentation defines code blocks. `return True` on line 3 must be indented inside the `if` block."
        ),
        Puzzle(
            id=3, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="Truthiness of Collections",
            code="print(bool([]), bool([0]))",
            question="What does this code print?",
            options=["True True", "False False", "False True", "True False"],
            correct_answer=3,
            explanation="Empty collections evaluate to False. A non-empty list `[0]` evaluates to True, even if its element is 0."
        ),
        Puzzle(
            id=4, difficulty=Difficulty.EASY, type=PuzzleType.BUG,
            title="Missing Colon",
            code="1| def greet(name)\n2|     message = f'Hi, {name}!'\n3|     return message\n4| \n5| print(greet('Alex'))",
            question="The code raises a SyntaxError. Which line is invalid?",
            options=["Line 1", "Line 2", "Line 3", "Line 5"],
            correct_answer=1,
            explanation="The function definition `def greet(name)` is missing a colon `:` at the end of line 1."
        ),
        Puzzle(
            id=5, difficulty=Difficulty.EASY, type=PuzzleType.OUTPUT,
            title="Division in Python 3",
            code="print(type(5 / 2))",
            question="What data type does `5 / 2` return?",
            options=["<class 'int'>", "<class 'float'>", "<class 'number'>", "<class 'double'>"],
            correct_answer=2,
            explanation="In Python 3, the `/` operator always returns a `float`, even when dividing evenly (e.g., 4 / 2 -> 2.0)."
        ),

        # --- MEDIUM ---
        Puzzle(
            id=6, difficulty=Difficulty.MEDIUM, type=PuzzleType.OUTPUT,
            title="Tricky Lists",
            code="a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            question="What will this code print?",
            options=["[1, 2, 3]", "[1, 2, 3, 4]", "Error", "None"],
            correct_answer=2,
            explanation="Variables are object references. `a` and `b` point to the same list in memory."
        ),
        Puzzle(
            id=7, difficulty=Difficulty.MEDIUM, type=PuzzleType.BUG,
            title="Dangerous Default Values",
            code="1| def add_item(item, items=[]):\n2|     items.append(item)\n3|     return items\n4| \n5| print(add_item(1))\n6| print(add_item(2))",
            question="The function persists data across calls instead of creating a new list. Which line contains the bug?",
            options=["Line 1", "Line 2", "Line 3", "Line 5"],
            correct_answer=1,
            explanation="Mutable default arguments (`items=[]`) are evaluated only once at definition time. You should use `items=None`."
        ),
        Puzzle(
            id=8, difficulty=Difficulty.MEDIUM, type=PuzzleType.OUTPUT,
            title="Nested Membership Test",
            code="items = [1, 2, [3, 4]]\nprint(3 in items)",
            question="What does `3 in items` evaluate to?",
            options=["True", "False", "TypeError", "None"],
            correct_answer=2,
            explanation="The `in` operator checks top-level items of the list. Number 3 is inside a nested list, so it evaluates to `False`."
        ),
        Puzzle(
            id=9, difficulty=Difficulty.MEDIUM, type=PuzzleType.BUG,
            title="String Immutability",
            code="1| greeting = 'hello world'\n2| greeting[0] = 'H'\n3| print(greeting)",
            question="The interpreter raises a TypeError. Which line is the cause?",
            options=["Line 1", "Line 2", "Line 3", "No error"],
            correct_answer=2,
            explanation="Strings in Python are immutable. You cannot assign to an index like `greeting[0] = 'H'`."
        ),

        # --- HARD ---
        Puzzle(
            id=10, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Closures and Late Binding",
            code="funcs = []\nfor i in range(3):\n    funcs.append(lambda: i)\n\nfor f in funcs:\n    print(f(), end=' ')",
            question="What will this code output?",
            options=["0 1 2", "2 2 2", "1 2 3", "NameError"],
            correct_answer=2,
            explanation="Lambda functions capture variable `i` by reference (late binding). When called, `i` has reached 2."
        ),
        Puzzle(
            id=11, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Finally Block Override",
            code="def compute():\n    try:\n        return 1\n    finally:\n        return 2\n\nprint(compute())",
            question="What will `compute()` return?",
            options=["1", "2", "SyntaxError", "1 2"],
            correct_answer=2,
            explanation="A `finally` clause executes right before exiting. Its `return 2` overwrites the earlier `return 1`."
        ),
        Puzzle(
            id=12, difficulty=Difficulty.HARD, type=PuzzleType.OUTPUT,
            title="Dictionary Key Collision",
            code="data = {1: 'Python', 1.0: 'LernPy', True: 'Awesome'}\nprint(len(data))",
            question="How many items will be in dictionary `data`?",
            options=["3", "2", "1", "TypeError"],
            correct_answer=3,
            explanation="In Python, `1 == 1.0 == True` and their hash values match. They represent the exact same dictionary key, overwriting each other."
        ),
        Puzzle(
            id=13, difficulty=Difficulty.HARD, type=PuzzleType.BUG,
            title="Immutable Tuple",
            code="1| record = (10, 20, [30, 40])\n2| record[2].append(50)\n3| record[0] = 99\n4| print(record)",
            question="On which line will a TypeError occur?",
            options=["Line 1", "Line 2", "Line 3", "Line 4"],
            correct_answer=3,
            explanation="Tuples are immutable. Assigning to `record[0]` raises a TypeError. Mutating the list inside the tuple on line 2 is completely valid."
        )
    ]
}
