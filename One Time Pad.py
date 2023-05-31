import string

def encrypt(plaintext, key_stream):
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char in string.ascii_lowercase:
            shift = ord(key_stream[i % len(key_stream)]) - ord('a')
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
    return ciphertext

def decrypt(ciphertext, key_stream):
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char in string.ascii_lowercase:
            shift = ord(key_stream[i % len(key_stream)]) - ord('a')
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += decrypted_char
    return plaintext

plaintext = "sendmoremoney"
key_stream = [8, 12, 1, 7, 23, 15, 21, 14, 11, 19, 2, 0, 9]

ciphertext = encrypt(plaintext, [chr(key + ord('a')) for key in key_stream])
print("Ciphertext:", ciphertext)



#find the key Using the ciphertext
target_plaintext = "cashnotneeded"

for i in range(len(ciphertext)):
    possible_key_stream = [(ord(ciphertext[i]) - ord(target_plaintext[i])) % 26 for i in range(len(ciphertext))]
    decrypted_text = decrypt(ciphertext, [chr(key + ord('a')) for key in possible_key_stream])
    if decrypted_text == target_plaintext:
        print("Key stream:", possible_key_stream)
        break
