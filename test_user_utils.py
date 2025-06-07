from user_utils import add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

from user_utils import is_even
def test_is_even():
    assert is_even (4) is True
    assert is_even(3) is False

from user_utils import max_of_three
def test_max_of_three():
    assert max_of_three(4,5,3) == 5

from user_utils import reverse_string
def test_reverse_string():
    assert reverse_string('hello') == 'olleh'

from user_utils import factorial
def test_factorial():
    assert factorial(3) == 6
    assert factorial(4) == 24

from user_utils import is_palindrome
def test_is_palindrome():
    assert is_palindrome('топот') is True
    assert is_palindrome('магазин') is False

from user_utils import count_vowels
def test_count_vowels():
    assert count_vowels ('apple') == 2
    assert count_vowels ('orange') == 3

from user_utils import from_Fibonacci
def test_from_Fibonacci():
    assert from_Fibonacci (1) == 2
    assert from_Fibonacci (2) == 3
    assert from_Fibonacci (3) == 5

from user_utils import remove_duplicates
def test_remove_duplicates():
    assert remove_duplicates ('Привет привет.Меня зовут Вася') == 'Привет.Меня зовут Вася'

from user_utils import flatten
def test_flatten():
    assert flatten ([
        [1,2,3],
        [4,5,6]
    ]) == (1,2,3,4,5,6)

from user_utils import get_common_elements
def test_get_common_elements():
    assert get_common_elements([1,2,3,4],[3,4,5,6]) == [3,4]
    assert get_common_elements([5,6,7],[6,7,9]) == [6,7]

from user_utils import is_anagram
def test_is_anagram():
    assert is_anagram(['древесница'],['сердцевина']) is True
    assert is_anagram(['яблоко'],['виноград']) is False

from user_utils import unique_words
def test_unique_words():
    assert unique_words('яблоко,апельсин,обезьяна,арбуз,сено,апельсин,обезьяна,арбуз') == 'яблоко, сено'

from user_utils import merge_dicts
def test_merge_dicts():
    assert merge_dicts({'name':'Roma'},{'age':'16'}) == {'name':'Roma','age':'16'}

from user_utils import group_by_parity
def test_group_by_parity():
    assert group_by_parity([2,4,6,8,10]) is even
    assert group_by_parity([1,3,5,7,9]) is odd

from user_utils import from_transportation
def test_from_transportation():
    assert from_transportation('привет мир') == 'мир привет'

from user_utils import