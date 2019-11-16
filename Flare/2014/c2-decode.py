#Note:Script is From Internet
e= r"\97\49\49\68\x4F\84\116\x68\97\x74\x44\x4F\x54\x6A\97\x76\x61\x35\x63\x72\97\x70\x41\84\x66\x6C\97\x72\x65\x44\65\x53\72\111\110\68\79\84\99\x6F\x6D"

res=''
e=e.split("\\")
for i in e:
	if i:
		if(i[0]== 'x'):
			res+= chr(int(i[1:3], 16))
		else:
			res+=chr(int(i))

print(res)



