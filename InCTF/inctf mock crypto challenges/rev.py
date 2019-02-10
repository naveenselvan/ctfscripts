
key=20
secret='7d7a7760726f4720667020664b567c202220604b47257a227c4b6320674b7c25674b7a20797169'

secret=bytearray.fromhex(secret).decode()
print(secret)





e=""
for i in secret:
	e+=chr(ord(i)^key)

print(e)
	


