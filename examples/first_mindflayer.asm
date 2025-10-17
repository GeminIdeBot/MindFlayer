section .data
    buffer db 0
section .bss
    mem resb 60000
section .text
    global _start
_start:
    mov edi, mem
    mov esi, mem + 30000
    mov byte [edi], 65
    inc edi
    dec edi
    mov al, byte [edi]
    xor al, 0xAA
    add al, 0x55
    mov byte [edi], al
    inc edi
    dec edi
    mov eax, 4
    mov ebx, 1
    mov ecx, edi
    mov edx, 1
    int 0x80
    inc edi
    mov eax, 1
    xor ebx, ebx
    int 0x80