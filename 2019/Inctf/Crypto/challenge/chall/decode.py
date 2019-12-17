import binascii


flag = open("ciphertext.txt").read()


for i in range(5):
	flag = binascii.unhexlify(flag)
	flag=(flag.decode('base64'))
	print("flag is "+flag)
