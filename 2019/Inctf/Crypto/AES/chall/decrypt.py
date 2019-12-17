from Crypto.Cipher import AES
import binascii

key = "fq3tjj#fm3)49faf"
flag = open("ciphertext.txt").read()
flag = binascii.unhexlify(flag)

obj1 = AES.new(key, AES.MODE_ECB)
ct = obj1.decrypt((flag))
open("flag.txt",'w').write(ct)
