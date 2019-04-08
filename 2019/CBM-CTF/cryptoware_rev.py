w=open('secretInfo')

cipher=(w.read())
w.close()
for i in range(0,255):
    fl=''
    for j in cipher:
        fl+=chr(i^ord(j))
        if 'cbmctf{' in fl:
            print("key is ",i)
            key=i
            #print(fl)
            break

flag=''

for j in cipher:
    flag+=chr(ord(j)^key)
    
print(flag)

