key=[137,80,78,71,13,10,26,10] #pngheadervalues xor known plaintext cipher gives key
key=key*2000    #simply brute size


file = open('blob.bin','rb')
cont = file.read()
file.close()

cipher=cont


intcipher=[]
for i in cipher:
    intcipher.append(ord(i))



fl=''
index=0
secondindex=1
encrypted=[]
try:
	for q in range(len(intcipher)):
	    fl+=chr(intcipher[secondindex]^(key[index%len(key)]))
            encrypted.append(intcipher[secondindex])
	    secondindex+=2
	    index+=1
except:
     pass


key=fl[:8]
print(key)

newkey=[]
for i in key:
    newkey.append(ord(i))

#print(newkey)

key=newkey


key=key*200000

index=0
fl=''
for q in encrypted:
    fl+=chr(q^(key[index%len(key)]))
    index+=1

print(len(fl))
fileo=open("flag.png","wb")
fileo.write(fl)
fileo.close()

#for i in te:
#    print(hex(i))
