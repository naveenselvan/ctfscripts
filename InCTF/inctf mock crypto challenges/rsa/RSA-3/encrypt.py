from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2


p = getPrime(512)
q = getPrime(512)
n = p*q

print(n)

