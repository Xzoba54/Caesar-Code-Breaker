from pathlib import Path

def import_probabilities(path: str | Path) -> dict[str, float]:
     ngrams = {}
     path = Path(path)
     if not path.is_file():
          raise FileNotFoundError(f"Error: File not found {path}")
     with open(path, "r") as file:
          for line in file.readlines():
               parts = line.strip().split(":")
               if len(parts) != 2:
                    raise ValueError(f"Error: Invalid file format in {path}")
               ngram, probability = parts
               if ngram == "":
                    raise ValueError(f"Error: Key not found in file {path}")
               if probability == "":
                    raise ValueError(f"Error: Value not found in file {path}")
               ngrams[ngram] = float(probability)
     return ngrams

def export_probabilities(path: str | Path, ngrams: dict[str, float], limit: int = 10000):
     path = Path(path)
     with open(path, "w") as file:
          k = 0
          for ngram, probability in ngrams.items():
               if k >= limit:
                    break
               k += 1
               file.write(f"{ngram}: {str(probability)}\n")