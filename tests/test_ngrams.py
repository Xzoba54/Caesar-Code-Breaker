from src.analysis.ngrams import normalize_ngrams_count, make_ngrams

def test_make_ngrams():
    assert make_ngrams("abab", 2) == {
        "ab": 2,
        "ba": 1,
    }


def test_make_ngrams_single_character():
    assert make_ngrams("abc", 1) == {
        "a": 1,
        "b": 1,
        "c": 1,
    }

def test_make_ngrams_n_equals_text_length():
    assert make_ngrams("abc", 3) == {
        "abc": 1,
    }

def test_make_ngrams_n_greater_than_text_length():
    assert make_ngrams("abc", 4) == {}

def test_make_ngrams_empty_text():
    assert make_ngrams("", 2) == {}


def test_make_ngrams_with_spaces():
    assert make_ngrams("a a", 2) == {
        "a ": 1,
        " a": 1,
    }


def test_normalize_ngrams_count():
    ngrams = {
        "ab": 2,
        "ba": 1,
    }

    assert normalize_ngrams_count(ngrams) == {
        "ab": round(2 / 3, 12),
        "ba": round(1 / 3, 12),
    }


def test_normalize_ngrams_count_equal_values():
    ngrams = {
        "aa": 2,
        "bb": 2,
        "cc": 2,
        "dd": 2,
    }

    assert normalize_ngrams_count(ngrams) == {
        "aa": 0.25,
        "bb": 0.25,
        "cc": 0.25,
        "dd": 0.25,
    }


def test_normalize_ngrams_count_single_ngram():
    assert normalize_ngrams_count({"abc": 5}) == {
        "abc": 1.0,
    }


def test_normalize_ngrams_count_rounding():
    ngrams = {
        "a": 1,
        "b": 1,
        "c": 1,
    }

    result = normalize_ngrams_count(ngrams)

    assert result == {
        "a": 0.333333333333,
        "b": 0.333333333333,
        "c": 0.333333333333,
    }