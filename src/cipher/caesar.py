def encrypt(plaintext: str, shift: int):
     ciphertext = ""

     for c in plaintext:
          if not c.isalnum():
               ciphertext += c
               continue
          ciphertext += chr(ord('a') + ((ord(c) - ord('a') + shift) % 26))
     return ciphertext


def decrypt(ciphertext):
     return ""