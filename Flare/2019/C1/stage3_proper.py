cipher=[95,193,50,12,127,228,98,6,215,46,200,106,251,121,186,119,109,73,35,14,20]
flag=''
array=[]
cat='QmFnZWxfQ2Fubm9u'  #Base64 Encoded Second Stage Flag Retrieved From The Dnspy

for i in range(0,256):
   array.append(i)  # Array With Values
 
j=0
num=0

def swap(a,b,c):   #Swapping Array
   temp = a[b]
   a[b] = a[c]
   a[c] = temp


#Construct Array With Proper Values
for i in range(0,256):
   num= num + ord(cat[j % len(cat)]) + array[j] & 255 
   swap(array,j,num)
   j=j+1

i=0
j=0

#Xor - Final Decryption Routine
for q in cipher:
      i= i + 1 & 255
      j= j + array[i] & 255
      swap(array,i,j)
      flag+=chr(q^(array[array[i] + array[j] & 0xFF]))
       
print("Third Stage Flag is "+flag)

