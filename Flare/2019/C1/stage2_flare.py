cipher=['\x03','"','"','"','%','\x14','\x0e','.','?','=',':','9']
count=0
flag=''
for i in cipher:
   flag+=chr((ord(i)^(65 + count *2)))
   print(count)
   count=count+1

print(flag)

