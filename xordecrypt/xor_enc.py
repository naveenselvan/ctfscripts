import os
import struct
import sys
def four_byte_xor(content,key):
    translated=""
    len_content=len(content)
    index=0
    while(index<len_content):
        data=content[index:index+4]
	if(len(data)!=4):
	    data= data + "\x00" *(4-len(data))
	    print(data)
	p=struct.unpack("I",data)[0]
       	translated+=struct.pack("I",p^key)
#        print(translated)
	index+=4
    return translated
in_file=open("en.bin",'rb')
out_file=open("dn.bin",'wb')
xor_key=0xEAD4AA34
rsrc_content=in_file.read()
decrypted_content=four_byte_xor(rsrc_content,xor_key)
out_file.write(decrypted_content)
