el='|#4b~W7h;Wj<5!k=on9b5?'


fl=''
for index in range(0,22):
    for j in range(0,150):
        if index & 1:
            if(j-4)^0xc == ord(el[index]):
                fl+=chr(j)
        else:
            if(j+4)^0xc == ord(el[index]):
               fl+=chr(j)

print(fl)
