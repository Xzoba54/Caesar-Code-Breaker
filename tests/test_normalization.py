from src.analysis.normalization import normalize

def test_normalization():
     with open("data/samples/raw_text.txt", "r") as file:
          print(file.readline())