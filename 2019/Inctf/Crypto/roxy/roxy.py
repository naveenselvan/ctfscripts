from itertools import cycle
from time import time
import os
from hashlib import md5

flag = "#"
# Guess the flag!
def xor(a,b):
    print(len(b))
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))

def hasho(sz):
    return os.urandom(sz)

def otp(sz):
    return md5(hasho(sz)).digest()

def encrypt(m):
    return xor(m,otp(24))

def package(m):
    _header = \
        "--Begin--"
    _timestamp = \
        str(time())
    _footer = \
        "--END--"
    return _header+"\n\r"+_timestamp+"\n\r"+m+"\n"+_footer

if __name__=="__main__":
    print encrypt(package(flag)).encode('hex')
