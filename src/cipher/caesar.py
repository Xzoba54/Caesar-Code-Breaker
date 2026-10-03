def encrypt(plaintext: str, shift: int):
     ciphertext = ""

     for c in plaintext:
          if not ("a" <= c and c <= "z"):
               ciphertext += c
          else:
               ciphertext += chr(ord("a") + ((ord(c) - ord("a") + shift) % 26))
     return ciphertext


def decrypt(ciphertext: str, shift: int):
     plaintext = ""

     for c in ciphertext:
          if not ("a" <= c and c <= "z"):
               plaintext += c
          else: 
               plaintext += chr(ord("a") + ((ord(c) - ord("a") - shift) % 26))
     return plaintext