import pytest
from solution import is_anagram
from hypothesis import given
from hypothesis import strategies as st

# Unit tests
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