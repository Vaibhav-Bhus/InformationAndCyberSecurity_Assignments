# Function to generate a random monoalphabetic cipher key
def generate_cipher_key():
    import random
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    return "".join(alphabet)


def monoalphabetic_encrypt(plaintext, cipher_key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = cipher_key[ord(char) - ord('A')].upper()
            else:
                encrypted_char = cipher_key[ord(char) - ord('a')].lower()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def monoalphabetic_decrypt(ciphertext, cipher_key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(cipher_key.upper().index(char) + ord('A'))
            else:
                decrypted_char = chr(cipher_key.lower().index(char) + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


plaintext = "This is a secret message."
cipher_key = generate_cipher_key()

ciphertext = monoalphabetic_encrypt(plaintext, cipher_key)
print("Encrypted ciphertext:", ciphertext)

decrypted_text = monoalphabetic_decrypt(ciphertext, cipher_key)
print("Decrypted plaintext:", decrypted_text)


