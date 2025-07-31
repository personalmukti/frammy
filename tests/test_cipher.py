import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from frammy.cipher import encrypt, decrypt


def test_encrypt_decrypt_roundtrip():
    plaintext = b"hello world"
    key = b"secret"
    ciphertext = encrypt(plaintext, key)
    assert ciphertext != plaintext
    assert decrypt(ciphertext, key) == plaintext
