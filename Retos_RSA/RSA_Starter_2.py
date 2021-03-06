
b = 12 # Base
e = 65537 # Exponente
p, q = 17, 23 # Primes numbers
N = p * q # Modulus

print(pow(b, e, N))