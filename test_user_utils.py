from user_utils import add, from_transportation, is_even, max_of_three, reverse_string, factorial, is_palindrome, \
    count_vowels, from_Fibonacci, remove_duplicates, flatten, get_common_elements, is_anagram, unique_words, \
    merge_dicts, group_by_parity


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_even():
    assert is_even (4) is True
    assert is_even(3) is False


def test_max_of_three():
    assert max_of_three(4,5,3) == 5


def test_reverse_string():
    assert reverse_string('hello') == 'olleh'

def test_factorial():
    assert factorial(3) == 6
    assert factorial(4) == 24


def test_is_palindrome():
    assert is_palindrome('топот') is True
    assert is_palindrome('магазин') is False


def test_count_vowels():
    assert count_vowels ('apple') == 2
    assert count_vowels ('orange') == 3


def test_from_Fibonacci():
    assert from_Fibonacci (1) == [0]
    assert from_Fibonacci (2) == [0,1]
    assert from_Fibonacci (3) == [0,1,1]


def test_remove_duplicates():
    assert remove_duplicates ([1,1,2,3,4,4]) == [1,2,3,4]


def test_flatten():
    assert flatten ([
        [1,2,3],
        [4,5,6]
    ]) == [1,2,3,4,5,6]


def test_get_common_elements():
    assert get_common_elements([1,2,3,4],[3,4,5,6]) == [3,4]
    assert get_common_elements([5,6,7],[6,7,9]) == [6,7]


def test_is_anagram():
    assert is_anagram('древесница','сердцевина') is True
    assert is_anagram('яблоко','виноград') is False


def test_unique_words():
    assert unique_words('привет привет как дела') == {'привет', 'как', 'дела'}


def test_merge_dicts():
    assert merge_dicts({'name':'Roma'},{'age':'16'}) == {'name':'Roma','age':'16'}

def test_group_by_parity():
    assert group_by_parity([2, 4, 6, 8, 10]) == {"even": [2, 4, 6, 8, 10], "odd": []}
    assert group_by_parity([1, 3, 5, 7, 9]) == {"even": [], "odd": [1, 3, 5, 7, 9]}
    assert group_by_parity([1, 2, 3, 4]) == {"even": [2, 4], "odd": [1, 3]}


def test_from_transportation():
    text = "привет мир"
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    result = from_transportation(matrix)
    assert result == expected, f"Ожидалось {expected}, но получено {result}"

def test_from_password():
    assert from_password ('Password1') == True
    assert from_password ('roma1') == False
    assert from_password ('apple') == False

def test_calculate_expression():
    assert calculate_expression ('2 + 2 * 3') == 8
    assert calculate_expression ('2 + 2 * 3') != 12