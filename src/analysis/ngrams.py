def make_ngrams(text: str, n: int) -> dict[str, int]:
     ngrams = {}
     i = 0
     k = len(text)
     while i < k - n + 1:
          ngram = text[i:i+n]
          if ngram not in ngrams:
               ngrams[ngram] = 1
          else:
               ngrams[ngram] += 1
          i+=1
     return ngrams

def total_ngrams(ngrams: dict[str, int]) -> int:
     return sum(ngrams.values())

def normalize_ngrams_count(ngrams: dict[str, int]) -> dict[str, float]:
     total = total_ngrams(ngrams)
     precision = 12

     ngram_frequency = {}
     for ngram, count in ngrams.items():
          ngram_frequency[ngram] = round(count / total, precision)
     return ngram_frequency

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