from analysis.frequency import calculate_frequency, normalize_frequency
from analysis.normalization import join_multiple_lines, normalize_for_ngrams

def main():
     lines = []
     with open("../data/samples/raw_text.txt", "r", encoding="utf-8") as file:
          lines = list(file)
     raw_text = join_multiple_lines(lines)
     normalized = normalize_for_ngrams(raw_text)
     return ""

if __name__ == "__main__":
     main()