import binascii
from itertools import cycle

cipher='c065c9a77e54ac8101343ea5417ae57ada7abcf62013f29d26335afa173ab626961abb9a6062f3df737d41ed043ae013bf7bfdf16b4ef1d126131ed13a0afd61'
str1 = binascii.unhexlify(cipher)

first=str1[:9]

print(len(first))

tempkey1='--Begin--'

print(len(tempkey1))
second=str1[57:]

print(len(second))
tempkey2='--END--'

print(len(tempkey2))
def xor (a,b):
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(a,(b)))


key1=xor(first,tempkey1)
key2=xor(second,tempkey2)


key=key1+key2

print(len(key))


def xor (a,b):
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(a,cycle(b)))


decrypt=xor(str1,key)

print(decrypt)


