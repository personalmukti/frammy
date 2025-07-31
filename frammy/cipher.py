from typing import Iterable


def encrypt(data: bytes, key: bytes) -> bytes:
    """Encrypt data using XOR cipher with the given key."""
    if not key:
        raise ValueError("Key must not be empty")
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def decrypt(data: bytes, key: bytes) -> bytes:
    """Decrypt data using XOR cipher with the given key."""
    return encrypt(data, key)
