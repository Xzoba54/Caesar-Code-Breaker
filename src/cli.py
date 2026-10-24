from analysis.normalization import import_training_raw_text, normalize_text
from analysis.ngrams import make_ngrams, normalize_ngrams
from analysis.model_io import export_probabilities, import_probabilities

def main():
     raw_text = import_training_raw_text("../data/samples/raw_text.txt")
     normalized_text = normalize_text(raw_text)

     bigrams_probability = normalize_ngrams(make_ngrams(normalized_text, 2))
     trigrams_probability = normalize_ngrams(make_ngrams(normalized_text, 3))

     characters_probability = normalize_ngrams(make_ngrams(normalized_text, 1))
     export_probabilities("../data/statistics/characters_probability.txt", characters_probability)
     export_probabilities("../data/statistics/bigrams_probability.txt", bigrams_probability)
     export_probabilities("../data/statistics/trigrams_probability.txt", trigrams_probability)

     try:
          import_probabilities("../data/statistics/trigrams_probability.txt")
     except ValueError as e:
          print(e)
     except FileNotFoundError as e:
          print(e)

if __name__ == "__main__":
     main()