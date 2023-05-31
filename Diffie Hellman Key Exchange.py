def diffie_hellman(p, g, a, b):
    # Alice public key
    x = (g ** a) % p

    # Bob public key
    y = (g ** b) % p

    # Alice shared secret key
    k_a = (y ** a) % p

    # Bob shared secret key
    k_b = (x ** b) % p

    # The shared secret keys should be the same
    if k_a == k_b:
        return k_a
    else:
        raise ValueError("Shared secret keys do not match.")


p = 23  # Prime number
g = 9  # Primitive root of p

# Alice's private key
a = 4

# Bob's private key
b = 3

shared_secret = diffie_hellman(p, g, a, b)
print("Shared secret key:", shared_secret)
