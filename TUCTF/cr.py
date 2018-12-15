from Crypto.Util.number import *
p=3004450991

q=3328247677


c = 6163751001056511617
n = 9999557031456097907



p=p-1
q=q-1

e=65537
t=p*q


import gmpy2

d = gmpy2.invert(e,t)


print((pow(c,d,n)))



