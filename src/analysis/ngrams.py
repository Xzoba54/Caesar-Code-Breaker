from collections import defaultdict

def make_ngrams(text: str, n: int) -> dict[str, int]:
     ngrams = defaultdict(int)
     i = 0
     k = len(text)
     while i < k - n + 1:
          ngram = text[i:i+n]
          if n == 1 and ngram == " " or ngram == "0":
               i += 1
               continue
          else:
               ngrams[ngram] += 1
          i+=1
     return ngrams

def normalize_counts(ngrams: dict[str, int]) -> dict[str, float]:
     total_ngrams = sum(ngrams.values())
     precision = 12
     normalized_ngrams = {}
     for ngram, count in ngrams.items():
          normalized_ngrams[ngram] = round(count / total_ngrams, precision)
     return normalized_ngrams