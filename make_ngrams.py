import argparse

def prepare_n_grams(text, n):
     ngrams = {}
     for i in range(0, len(text) - n + 1):
          gram = text[i:i + n]
          if gram not in ngrams:
               ngrams[gram] = 1
          else:
               ngrams[gram] += 1
     return ngrams

def make_probability(ngrams, sum_of_ngrams: float):
     with open("ngrams_probability.txt", "w", encoding="utf-8") as writer:
          for key, value in ngrams.items():
               probability = value / sum_of_ngrams
               writer.write(f"{key} {probability}\n")

if __name__ == "__main__":
     with open("plaintext.txt", "r", encoding="utf-8") as file:
          plaintext = file.read()

     parser = argparse.ArgumentParser()
     parser.add_argument("-n", type=int, default=3)
     args = parser.parse_args()

     n = args.n
     res = prepare_n_grams(plaintext, n)

     size = len(res)
     sum_of_ngrams = len(plaintext) - n
     sorted_ngrams = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
     
     with open("ngrams.txt", "w", encoding="utf-8") as writer:
          writer.write(str(sum_of_ngrams) + "\n")
          for key, value in sorted_ngrams.items():
               writer.write(f"{key}: {value}\n")
     print("ngrams saved to ngrams.txt")
     print(f"TOTAL {size} ngrams")
     print(f"TOTAL sum of {n}-grams {sum_of_ngrams}")

     make_probability(sorted_ngrams, sum_of_ngrams)
     print("ngrams probability saved to ngrams_probability.txt")