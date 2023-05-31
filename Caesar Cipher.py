def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26  
            if mode == "encrypt":
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            else:  
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97)
            result += shifted_char
        else:
            result += char
    return result


def main():
    text = input("Enter text to encrypt/decrypt: ")
    key = int(input("Enter key (shift value): "))
    mode = input("Enter mode (encrypt/decrypt): ")
    result = caesar_cipher(text, key, mode)
    print("Result: ", result)
        


if __name__ == "__main__":
    main()