from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import os

def getTwinPrime():
	while True:
		p = getPrime(1024)
		if isPrime(p+2):
			return p


def genKey():
	p = getTwinPrime()
	q = getTwinPrime()

	n1 = p*q
	n2 = (p+2)*(q+2)

	e = 65537

	phin1 = (p-1)*(q-1)
	phin2 = (p+1)*(q+1)

	d1 = inverse(e, phin1)
	d2 = inverse(e, phin2)

	key1 = RSA.construct((n1, e, d1))
	key2 = RSA.construct((n2, e, d2))

	if n1 < n2:
		return (key1, key2)
	else:
		return (key2, key1)	


rsa1, rsa2 = genKey()	

with open("flag.txt", "r") as f:
	flag = f.read()
	print(flag)

c = bytes_to_long(flag)
c = rsa1.encrypt(c, 0)[0]
c = rsa2.encrypt(c, 0)[0]	

with open("key1.txt", "w") as f:
	f.write("%d\n" % rsa1.n)
	f.write("%d\n" % rsa1.e)

with open("key2.txt", "w") as f:
	f.write("%d\n" % rsa2.n)
	f.write("%d\n " % rsa2.e)

with open("ciphertext.txt") as f:
	f.write("%d\n" % c)



