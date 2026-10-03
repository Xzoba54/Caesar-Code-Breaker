from analysis import normalize_for_ngrams, join_multiple_lines

def main():
     lines = []
     with open("../data/samples/raw_text.txt", "r", encoding="utf-8") as file:
          lines = list(file)
     raw_text = join_multiple_lines(lines)
     normalized = normalize_for_ngrams(raw_text)
     print(normalized)
     return ""

if __name__ == "__main__":
     main()