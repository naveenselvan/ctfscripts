original = 'abcdefghijklmnopqrstuv-xyz0{23456789'

enc_key =  'XYZ01234567890ABCDEFGHVJKLLMNOPQRSTU'

enc_flag =  '4EZF2M7O5F4V9P7OEVFDPE4VDOO'

dec_flag=''

for i in range(len(enc_flag)):
	for q in range(len(enc_key)):
		if enc_flag[i]==enc_key[q]:
 		    dec_flag+=(original[q])


print(dec_flag[:-1]+"}")
