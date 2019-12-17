import binascii

input_string = '1314190e1c1001024a0825194e145d0e251849251f4e091316032518084a11491407'
str1 = binascii.unhexlify(input_string)


fl=''
for i in str1:
	fl+=chr(ord(i)^ord('z'))


print(fl)
