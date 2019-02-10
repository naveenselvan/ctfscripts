from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2




f = open("ciphertext.txt", "r")
print(bytes_to_long(f.read()))

