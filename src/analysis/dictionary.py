from collections import defaultdict

def count_words(text: str, min_characters: int = 2) -> dict[str, int]:
     words_count = defaultdict(int)
     words = text.split(" ")
     for word in words:
          if len(word) < min_characters:
               continue
          words_count[word] += 1
     return words_count