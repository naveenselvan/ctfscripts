w=open('flag','rb')

content=w.read()


w.close()


for i in content:
    print(ord(i))
