from analysis.normalization import import_training_raw_text, normalize_text
from analysis.ngrams import make_ngrams, normalize_counts
from analysis.dictionary import count_words

def main():
     raw_text = import_training_raw_text("../data/samples/raw_text.txt")
     normalized_text = normalize_text(raw_text)

     bigrams_probability = normalize_counts(make_ngrams(normalized_text, 2))
     trigrams_probability = normalize_counts(make_ngrams(normalized_text, 3))
     characters_probability = normalize_counts(make_ngrams(normalized_text, 1))
     words_probability = normalize_counts(count_words(normalized_text))

if __name__ == "__main__":
     main()