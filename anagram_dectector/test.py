import pytest
from solution import group_anagrams
from solution import is_anagram
from solution import find_anagrams
from hypothesis import given
from hypothesis import strategies as st


# Part 1: Unit tests
@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("line", "line", True),
        ("", "", True),
        ("run", "nru", True),
        ("bank", "knab", True),
        ("bank", "banr", False),
    ]
)
def test_anagram_pairs(word1, word2, expected):
    assert is_anagram(word1, word2) == expected, f"Expected is_anagram for {word1} and {word2} to be {expected}"

# Property based tests
@given(st.text(), st.text())
def test_property_anagrams_diff_lengths(word_1, word_2):
    if len(word_1) != len(word_2):
        assert is_anagram(word_1, word_2) == False

@given(st.text(), st.text())
def test_property_anagrams_missing_letters(word_1, word_2):
    for char in word_1:
        if char not in word_2:
            assert is_anagram(word_1, word_2) == False

@given(st.text(), st.text())
def test_property_anagrams_diff_lengths(word_1, word_2):
    assert is_anagram(word_1, word_2) == is_anagram(word_2, word_1)

# Part 2: Unit Tests
@pytest.mark.parametrize(
    "target, words, expected",
    [
        ("line", ["line"], ["line"]),
        ("run", ["run"], ["run"]),
        ("run", ["run", "run", "bob"], ["run", "run"]),
        ("run", ["nru", "bob"], ["nru"]),
        ("line", ["bob"], []),
        ("run", ["run", "nru", "urn", "nrus"], ["run", "nru", "urn"]),
    ]
)
def test_find_anagrams(target: str, words: list[str], expected: bool):
    assert find_anagrams(target, words) == expected

@given(st.text(), st.lists(st.text()))
def test_property_output_list_length(target: str, words: list[str]):
    assert len(find_anagrams(target, words)) <= len(words)

@given(st.text(), st.lists(st.text()))
def test_property_output_list_word_length(target: str, words: list[str]):
    for word in find_anagrams(target, words):
        assert len(word) == len(target)

@given(st.text(), st.lists(st.text()))
def test_property_output_list_is_anagram(target: str, words: list[str]):
    for word in find_anagrams(target, words):
        assert is_anagram(word, target)


@pytest.mark.parametrize(
    "input, expected",
    [
        ([], []),
        (["eat", "eat", "bob"], [["eat", "eat"], ["bob"]]),
        (["eat", "tea", "bob", "bbo", "shoe"], [["eat", "tea"], ["bob", "bbo"], ["shoe"]]),
        (["", ""], [["", ""]])
    ]
)
def test_find_anagrams(input: list[str], expected: list[list[str]]):
    assert group_anagrams(input) == expected

@given(st.lists(st.text()))
def test_property_total_word_count(input: list[str]):
    output = group_anagrams(input)
    final_sum = 0
    for group in output:
        final_sum += len(group)
    assert len(input) == final_sum