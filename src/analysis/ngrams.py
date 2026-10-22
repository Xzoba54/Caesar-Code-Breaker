from collections import defaultdict

def make_ngrams(text: str, n: int) -> dict[str, int]:
     ngrams = defaultdict(int)
     i = 0
     k = len(text)
     while i < k - n + 1:
          ngram = text[i:i+n]
          ngrams[ngram] += 1
          i+=1
     return ngrams

def normalize_ngrams(ngrams: dict[str, int]) -> dict[str, float]:
     total_ngrams = sum(ngrams.values())
     precision = 12

     normalized_ngrams = {}
     for ngram, count in ngrams.items():
          normalized_ngrams[ngram] = round(count / total_ngrams, precision)
     return normalized_ngrams

def export_ngrams(path: str, ngrams: dict[str, float]):
     with open(path, "w") as file:
          for ngram, probability in ngrams.items():
               file.write(f"{ngram}: {str(probability)}\n")

def import_ngrams(path: str) -> dict[str, float]:
     ngrams = {}
     with open(path, "r") as file:
          for line in file.readlines():
               ngram, probability = line.strip().split(":")
               ngrams[ngram] = float(probability)
     return ngrams