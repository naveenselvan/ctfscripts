global main
section .data
source  db "PLaying With Strings",0
len equ $-source

section .bss
destination resb 30


section .text

main:
   mov ecx,len
   mov esi,source
   mov edi,destination
   cld
   rep movsb
   mov	edx,len        ;message length
   mov	ecx,destination	        ;message to write
   mov	ebx,1	        ;file descriptor (stdout)
   mov	eax,4	        ;system call number (sys_write)
   int	0x80	        ;call kernel

   mov eax,1
   int 0x80            

   



