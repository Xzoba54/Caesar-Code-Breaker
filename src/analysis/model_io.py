from pathlib import Path
from heapq import nlargest

def import_probabilities(path: str | Path) -> dict[str, float]:
     probabilities = {}
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
               probabilities[ngram] = float(probability)
     return probabilities

def export_probabilities(path: str | Path, probabilities: dict[str, float], limit: int = 10000):
     path = Path(path)
     sorted_probabilities = dict(nlargest(limit, probabilities.items(), lambda x: x[1]))
     with open(path, "w") as file:
          k = 0
          for ngram, probability in sorted_probabilities.items():
               if k >= limit:
                    break
               k += 1
               file.write(f"{ngram}: {str(probability)}\n")