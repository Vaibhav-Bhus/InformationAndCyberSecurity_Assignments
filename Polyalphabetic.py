def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    i = 0
    for char in plaintext:
        if char.isalpha():
            key_char = key[i % len(key)]
            ciphertext += chr(((ord(char) + ord(key_char) - 2 * ord('A')) % 26) + ord('A'))
            i += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    i = 0
    for char in ciphertext:
        if char.isalpha():
            key_char = key[i % len(key)]
            plaintext += chr(((ord(char) - ord(key_char) + 26) % 26) + ord('A'))
            i += 1
        else:
            plaintext += char
    return plaintext

plaintext = "encryption"
key = "leg"
ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted message:", ciphertext)
decrypted_plaintext = vigenere_decrypt(ciphertext, key)
print("Decrypted message:", decrypted_plaintext)
