section .data
    buffer db 0
section .bss
    mem resb 60000
section .text
    global _start
_start:
    mov edi, mem
    mov esi, mem + 30000
    mov ebp, mem + 50000
    mov eax, 3
    mov ebx, 0
    mov ecx, buffer
    mov edx, 10
    int 0x80
    xor eax, eax
    xor ebx, ebx
    mov ecx, buffer
read_digit_loop:
    mov bl, byte [ecx]
    cmp bl, 0x0A
    je end_read_digit
    cmp bl, '0'
    jl end_read_digit
    cmp bl, '9'
    jg end_read_digit
    sub bl, '0'
    mov bh, 10
    mul bh
    add al, bl
    inc ecx
    jmp read_digit_loop
end_read_digit:
    mov byte [edi], al
    inc edi
    mov byte [edi], 127
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