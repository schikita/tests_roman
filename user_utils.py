def add(a: int, b: int) -> int:
    """Сложение двух чисел"""
    return a + b

def is_even(n: int) -> bool:
    """Проверка, чётное ли число"""
    return n % 2 == 0


def max_of_three(a: int, b: int, c: int) -> int:
    """Максимум из трёх чисел"""
    if a > b > c:
        return a
    elif b > c:
        return b
    else:
        return c

def reverse_string(s: str) -> str:
    """Переворачивает строку"""
    return s[::-1]


def factorial(n: int) -> int:
    """Вычисляет факториал"""
    if n <= 0:
        return 1
    return factorial(n -1) * n

def is_palindrome(s: str) -> bool:
    """Проверка, является ли строка палиндромом"""
    return s == s[::-1]

def count_vowels(s: str) -> int:
    """Подсчёт гласных"""
    vowels = 'aeuioAEUIO'
    return sum (1 for char in s if char in vowels )

def from_Fibonacci (n: int) -> list[int]:
    """Генерация последовательности Фибоначчи длины n"""
    result = [0, 1]
    while len(result) < n:
        result.append (result[-1] + result[-2])
    return result [:n]

def remove_duplicates(lst: list[int]) -> list[int]:
    """Удаление дубликатов из списка"""
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

def flatten(matrix: list[list[int]]) -> list[int]:
    """Преобразование матрицы в плоский список"""
    return [item for row in matrix for item in row]

def get_common_elements(a: list[int], b: list[int]) -> list[int]:
    """Общие элементы двух списков"""
    return list(dict.fromkeys([x for x in a if x in b]))

def is_anagram(a: str, b: str) -> bool:
    """Проверка, являются ли строки анаграммами"""
    return sorted(a.lower()) == sorted(b.lower())

def unique_words(text: str) -> set[str]:
    """Возвращает уникальные слова из строки"""
    words = text.lower().split()
    return set(word.strip(".,!?;:()[]\"'") for word in words)

def merge_dicts(d1: dict, d2: dict) -> dict:
    """Объединяет два словаря"""
    d1.update(d2)
    return d1

d1 = {'d1': 1}
d2 = {'d2': 1}

print(merge_dicts(d1, d2))

def group_by_parity(lst: list[int]) -> dict[str, list[int]]:
    """Разделение списка на чётные и нечётные"""
    result = {
        "even": [],
        "odd": []
    }
    for number in lst:
        if number % 2 == 0:
            result["even"].append(number)
        else:
            result["odd"].append(number)
    return result

def from_transportation(matrix: list[list[int]]) -> list[list[int]]:
    """Транспонирование матрицы"""
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]

def from_password(pwd: str) -> bool:
    if len(pwd) < 8:
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    if not any(char.isupper() for char in pwd):
        return False
    return True
    """
    Проверка пароля по условиям:
    - не меньше 8 символов
    - есть цифра
    - есть заглавная буква
    """


def parse_csv_row(row: str) -> list[str]:
    """Разделяет CSV-строку по запятым, учитывая кавычки"""


def calculate_expression(expr: str) -> float:
    """Вычисляет выражение вида '2 + 2 * 3' (без eval)"""
    # Тут будет код