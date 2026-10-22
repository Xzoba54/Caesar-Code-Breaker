from collections import defaultdict

def calculate_frequency(text: str) -> dict[chr, int]:
     frequency = defaultdict(int)
     for c in text:
          frequency[c] += 1
     return frequency

def normalize_frequency(frequency: dict[chr, int]) -> dict[chr, float]:
     total_characters = sum(frequency.values())
     precision = 12

     normalized_frequency = {}
     for c, count in frequency.items():
          normalize_frequency[c] = round(count / total_characters, precision)
     return normalized_frequency

def export_frequency(path: str, normalized_frequency: dict[chr, float]):
     with open(path, "w") as file:
          for c, probability in normalized_frequency.items():
               file.write(f"{c}: {str(probability)}\n")