bits 32
extern printf
global main

section .data
    message db "Hello world!!", 10, 0

section .text

main:
    push dword message
    call printf 
    add esp, 4 
    ret
