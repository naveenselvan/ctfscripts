from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2
e=open('ciphertext.txt','r')

e=bytes_to_long	(e.read())

print(e)
