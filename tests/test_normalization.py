from src.analysis.normalization import normalize_for_ngrams

def test_normalization():
     text = "Hello World, test! 123 a!C"

     assert normalize_for_ngrams(text) == "hello world test 0 ac"