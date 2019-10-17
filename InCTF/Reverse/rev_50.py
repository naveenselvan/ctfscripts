cipher='FaZmk^'

for count in range(1,10):
   fl=''
   for i in cipher:
        for j in range(33,256):
            temp= (j ^ count)-18
            if chr(temp) ==i:
                fl+=(chr(j))
   print(count)
   print(fl)
   print "code = "+ str((16-count)*306783371)







cip1='asgeiszknc'
cip2='qcwuycj{~s'


def xor (a,b):
    return " ".join(hex(ord(a)^ord(b)) for a,b in zip(a,b))

decrypt =xor(cip1,cip2)
print(decrypt)

