import pytest

from src.analysis.normalization import normalize_text, normalize_numbers

def test_converts_text_to_lowercase():
        assert normalize_text("HeLLo WoRLD") == "hello world"

def test_removes_punctuation():
    assert normalize_text("hello, world!") == "hello world"

def test_preserves_spaces_when_requested():
    assert normalize_text(
        "Hello World"
    ) == "hello world"

def test_normalizes_numbers():
    assert normalize_text("I have 123 apples") == "i have 0 apples"

def test_preserves_spaces_and_normalizes_numbers():
    assert normalize_text(
        "I have 123 apples"
    ) == "i have 0 apples"

def test_handles_empty_string():
    assert normalize_text("") == ""

def test_handles_only_punctuation():
    assert normalize_text("!@#$%^&*()") == ""

def test_handles_only_numbers():
    assert normalize_text("123 456 789") == "0 0 0"

@pytest.mark.parametrize(
   ("text", "expected"),
   [
       ("123", "0"),
       ("abc123def", "abc0def"),
       ("12 34", "0 0"),
       ("a1b2c3", "a0b0c0"),
       ("123abc456", "0abc0"),
       ("", ""),
       ("abc", "abc"),
       ("000", "0"),
       ("12.34", "0.0"),
       ("123 ", "0 "),
   ],
)
def test_normalizes_digit_sequences(text, expected):
     assert normalize_numbers(text) == expected 