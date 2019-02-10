from Crypto.Cipher import AES

key = "\xa2q\x8bu6Y\xa1\rT\xb7\xce\x86\x81S\xf2\xfc"
flag = open("ciphertext.txt").read()
obj1 = AES.new(key, AES.MODE_ECB)
ct = obj1.decrypt((flag))
open("flag.txt",'w').write(ct)
