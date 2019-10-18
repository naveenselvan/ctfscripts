global main
section .data
file_name          db  "/home/ubuntu/Desktop/test/input.txt",0

section .text

main:
    mov ebx, file_name   ; filename
    xor eax,eax         ; zeros the eax
   mov al,10           ; delete system call
    int 80h             ; Call Kernel

    mov eax, 1                  ; exit system call value
    xor ebx,ebx                  ; exit return code
    int 80h                     ; Call the kernel




