section .data
    buffer db 0
section .bss
    mem resb 60000
section .text
    global _start
_start:
    mov edi, mem
    mov esi, mem + 30000
    mov byte [edi], 104
    inc edi
    dec edi
    mov al, byte [edi]
    mov bl, 5
    mul bl
    xor al, 0x77
    mov bl, byte [edi]
    and bl, 0x11
    add al, bl
    mov byte [edi], al
    inc edi
    dec edi
    mov al, byte [edi]
    test al, 1
    jz L1
    jmp L2
L1:
    mov bl, byte [edi-1]
    mov cl, byte [edi]
    mov byte [edi-1], cl
    mov byte [edi], bl
    jmp L3
L2:
    mov byte [esi + 3132], 0
    jmp L3
L3:
    inc edi
    dec edi
    mov bl, byte [edi]
    dec edi
    mov al, byte [edi]
    mov cl, al
    or cl, bl
    mov dh, al
    xor dh, bl
    sub cl, dh
    mov byte [edi], cl
    mov cl, al
    and cl, bl
    mov dh, al
    or dh, bl
    add cl, dh
    inc edi
    mov byte [edi], cl
    inc edi
    dec edi
    dec edi
    mov bl, byte [edi]
    dec edi
    mov al, byte [edi]
    mov cl, al
    xor cl, bl
    mov dh, al
    and dh, bl
    add cl, dh
    mov dh, bl
    or dh, al
    add cl, dh
    mov byte [edi], cl
    inc edi
    dec edi
    mov eax, 4
    mov ebx, 1
    mov ecx, edi
    mov edx, 1
    int 0x80
    inc edi
    dec edi
    mov al, byte [edi]
    inc esi
    mov byte [esi], al
L4:
    dec edi
    cmp byte [edi], 0
    je L5
    inc edi
    dec edi
    cmp byte [edi], 0
    jne L4
    inc edi
L5:
    mov eax, 1
    xor ebx, ebx
    int 0x80