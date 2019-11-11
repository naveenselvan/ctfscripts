e='CDI^LQdO]hCouxO|oXyOuoDMcDOoXW'

for q in range(1,256):
    fl=''
    for i in e:
        fl+=chr(ord(i)^q)
    if 'inctf{' in fl:
    	print(fl)
        print(chr(q))
