def affine_cipher(text, key1, key2, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key1 % 26  
            if mode == "encrypt":
                shifted_char = chr((key2 * (ord(char) - 65) + shift) % 26 + 65) if char.isupper() else chr((key2 * (ord(char) - 97) + shift) % 26 + 97)
            else:  
                try:
                    inverse = pow(key2, -1, 26)  
                except ValueError:
                    return "Error: key2 does not have a modular multiplicative inverse"
                shifted_char = chr((inverse * (ord(char) - 65 - shift)) % 26 + 65) if char.isupper() else chr((inverse * (ord(char) - 97 - shift)) % 26 + 97)
            result += shifted_char
        else:
            result += char
    return result


def main():
    text = input("Enter text to encrypt/decrypt: ")
    key1 = int(input("Enter key1 (multiplicative value): "))
    key2 = int(input("Enter key2 (shift value): "))
    mode = input("Enter mode (encrypt/decrypt): ")
    result = affine_cipher(text, key1, key2, mode)
    print("Result: ", result)

if __name__ == "__main__":
    main()