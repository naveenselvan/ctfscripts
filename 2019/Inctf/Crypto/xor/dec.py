import binascii
input_string = '11161b0c1e12031d0c270c0d271a0a0d0c1d272d271f170c27110c270a0c05'
str1 = binascii.unhexlify(input_string)


for i in range(0,255):
	str2=""
	for j in range(len(str1)):
		str2 += chr(ord( str1[j] ) ^ i)
	if 'inc' in str2:
        	print(str2)
