from Crypto.Util.number import *



m='metaphor Gerard gangster avocate melon'


print(bytes_to_long(m))





e = 65537
m = 88379461301359
n=9220560877693054349



print(pow(m,e,n))


from Crypto.Util.number import *

import gmpy2


p = 3445246939
q = 2443734731

e = 65537
c = 10626995461229291840988848739856549950759742995569449618301942263409489663664076282188883718369550472747640751159068205711394337814755036377493720378756757576694834155677852315604426114598076009996976101021691356371991518974426333878423159949773442282609526677144926382131388815922985034657787207533067845012

t = (p-1)*(q-1)
n = p*q

# returns d value such that e * d == 1 modulo t, or 0 if no such y exists.
d = gmpy2.invert(e,t)


print(d)
# Decryption
#decimalmessage = pow(c,d,n)
#print(long_to_bytes(decimalmessage))

import math


A=11464686656164734281
P=math.floor(math.sqrt(11464686656164734281))
print("Value of P",P)


n = 11464686656164734281

P=3385954319


i=0

while (i < 100):
	P = P-2
	print(int(P,A%P))
	
	if A%P ==0:
		print("found",P)
	i+=1
	






