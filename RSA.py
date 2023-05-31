import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    else:
        return x % m


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


p = 17
q = 11
n = p * q
phi_n = (p - 1) * (q - 1)
e = 7
d = mod_inverse(e, phi_n)

public_key = (e, n)
private_key = (d, n)

message = 88

ciphertext = encrypt(message, public_key)
print("Encrypted message:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
