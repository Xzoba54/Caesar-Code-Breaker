import sys
import math

def cesar_encrypt(plaintext: str, key):
     res = ""

     for c in plaintext:
          base = ord("A") if c.isupper() else ord("a")
          char = ord(c)
          encrypted = chr((char - base + key) % 26 + base)
          res += encrypted
     return res

def cesar_decrypt(ciphertext: str, key):
     res = ""

     for c in ciphertext:
          if c == " ":
               res += " "
               continue

          base = ord("A") if c.isupper() else ord("a")
          char = ord(c)
          decrypted = chr((char - base - key) % 26 + base)
          res += decrypted
     return res

def cesar_breaker(ciphertext):
     list_of_encrypted = []
     for key in range(0, 26):
          encrypted = cesar_decrypt(ciphertext, key)
          list_of_encrypted.append(encrypted)
     return list_of_encrypted

def import_probability(filename, n):
     probability = {}
     with open(filename, "r", encoding="utf-8") as file:
          for line in file.readlines():
               ngram = line[:n]
               ngram_probability = float(line[n:].strip())
               probability[ngram] = ngram_probability
     return probability

if __name__ == "__main__":
     ciphertext = sys.argv[1]
     res = cesar_breaker(ciphertext)

     n = 3
     probability = import_probability("ngrams_probability.txt", n)

     table = {}
     for t in res:
          total_probability = 0
          for i in range(0, len(t) - n + 1):
               gram = t[i:i + n]
               if gram not in probability:
                    total_probability += math.log10(1e-10)
                    continue

               total_probability += math.log10(probability[gram])
          table[t] = total_probability

     sorted_encyprted = list(sorted(table.items(), key=lambda x: x[1], reverse=True))

     print(f"HASH       \t{ciphertext}\n")
     print(f"BEST match:\t{sorted_encyprted[0][0]}")
     print(f"Score:     \t{sorted_encyprted[0][1]}")
     print("\n\n")

     for text, prob in sorted_encyprted:
          print(f"{text}\t{prob}")
     
