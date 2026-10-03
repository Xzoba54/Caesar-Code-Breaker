from src.cipher.caesar import encrypt, decrypt

def test_encrypt():
     assert encrypt("abc", 2) == "cde"
     assert encrypt('a', 27) == "b"

def test_decrypt():
     assert decrypt("cde", 2) == "abc"
     assert decrypt("w", 27) == "v"

def test_encrypt_and_decrypt():
     plaintext = "hello world 123 xyz!"
     shift = 7

     ciphertext = encrypt(plaintext, shift)
     decrypted = decrypt(ciphertext, shift)

     assert plaintext == decrypted