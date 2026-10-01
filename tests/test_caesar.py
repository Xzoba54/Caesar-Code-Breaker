from src.cipher.caesar import encrypt
import pytest

def test_encrypt():
     assert encrypt("abc", 2) == "cde"
     assert encrypt('a', 27) == "b"

def test_decrypt():
     assert 1 == 1