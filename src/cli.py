from analysis.normalization import import_training_raw_text, normalize_text
from analysis.ngrams import make_ngrams, normalize_ngrams
from analysis.frequency import expected_counts, chi_square

def main():
     raw_text = import_training_raw_text("../data/samples/raw_text.txt")
     normalized_text = normalize_text(raw_text)

     bigrams_probability = normalize_ngrams(make_ngrams(normalized_text, 2))
     trigrams_probability = normalize_ngrams(make_ngrams(normalized_text, 3))

     characters_probability = normalize_ngrams(make_ngrams(normalized_text, 1))

if __name__ == "__main__":
     main()