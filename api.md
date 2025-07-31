# Frammy API Documentation

This document provides basic information on accessing the API exposed by the Frammy framework.

## `encrypt(data: bytes, key: bytes) -> bytes`

Encrypts arbitrary byte data using an XOR cipher with the given key.

- `data` - the plaintext data to encrypt
- `key` - the secret key used for the XOR operation. It must not be empty.

Returns the encrypted bytes.

## `decrypt(data: bytes, key: bytes) -> bytes`

Performs decryption using the same XOR mechanism as `encrypt`.

- `data` - the ciphertext to decrypt
- `key` - the same secret key that was used for encryption

Returns the original plaintext bytes.

