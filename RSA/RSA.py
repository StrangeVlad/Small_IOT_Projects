import random
from math import gcd
from sympy import randprime

class RSA:
    def __init__(self, p=None, q=None, prime_range=(100, 300)):
        self.prime_start, self.prime_end = prime_range

        # Generate random primes if none provided
        if p is None:
            p = self.generate_prime()
        if q is None or q == p:
            q = self.generate_prime()
            while q == p:
                q = self.generate_prime()

        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)

        # Generate public key exponent e such that gcd(e, phi) = 1
        self.e = random.randint(2, self.phi - 1)
        while gcd(self.e, self.phi) != 1:
            self.e = random.randint(2, self.phi - 1)

        # Compute private exponent d
        self.d = pow(self.e, -1, self.phi)

        self.public_key = (self.e, self.n)
        self.private_key = (self.d, self.n)

    def generate_prime(self):
        return randprime(self.prime_start, self.prime_end)

    def encrypt(self, message, public_key=None):
        if public_key is None:
            public_key = self.public_key
        e, n = public_key
        m = [ord(char) for char in message]
        c = [pow(char, e, n) for char in m]
        return c

    def decrypt(self, ciphertext, private_key=None):
        if private_key is None:
            private_key = self.private_key
        d, n = private_key
        m = [pow(char, d, n) for char in ciphertext]
        message = ''.join(chr(char) for char in m)
        return message

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key
