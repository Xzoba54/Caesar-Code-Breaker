from analysis import normalize_for_ngrams, join_multiple_lines, make_ngrams, total_ngrams, normalize_ngrams_count, export_ngrams, import_ngrams

def main():
     lines = []
     with open("../data/samples/raw_text.txt", "r", encoding="utf-8") as file:
          lines = list(file)
     raw_text = join_multiple_lines(lines)
     normalized = normalize_for_ngrams(raw_text)
     bigrams = make_ngrams(normalized, 2)
     ngrams_frequency = normalize_ngrams_count(bigrams)
     # print(bigrams)
     # print(normalize_ngrams_count(bigrams))
     export_ngrams("../data/statistics/bigrams_frequency.txt", ngrams_frequency)

     trigrams = make_ngrams(normalized, 3)
     trigrams_frequency = normalize_ngrams_count(trigrams)
     export_ngrams("../data/statistics/trigrams_frequency.txt", trigrams_frequency)

     import_ngrams("../data/statistics/bigrams_frequency.txt")
     return ""

if __name__ == "__main__":
     main()