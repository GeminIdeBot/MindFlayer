import random

class CodeGenerator:
    def __init__(self):
        self.assembly_code = []
        self.data_segment = []
        self.label_counter = 0
        self.loop_stack = [] # Стек для хранения меток циклов
        self.main_stack_ptr = 0 # Указатель на главный стек (сознание)
        self.sub_stack_ptr = 30000 # Указатель на вспомогательный стек (подсознание), начинаем с конца памяти

    def _generate_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"

    def generate(self, tokens):
        self.assembly_code.append("section .data")
        self.assembly_code.append("    buffer db 0") # Для операций ввода/вывода
        self.assembly_code.append("section .bss")
        self.assembly_code.append("    mem resb 60000") # 30000 ячеек для сознания, 30000 для подсознания
        self.assembly_code.append("section .text")
        self.assembly_code.append("    global _start")
        self.assembly_code.append("_start:")
        self.assembly_code.append("    mov edi, mem") # edi - указатель на текущую ячейку памяти (сознания)
        self.assembly_code.append("    mov esi, mem + 30000") # esi - указатель на подсознание

        for token in tokens:
            if token == 'F': # Flash: Генерирует случайное число (0-255) и помещает его в "сознание"
                self.assembly_code.append(f"    mov byte [edi], {random.randint(0, 255)}")
                self.assembly_code.append("    inc edi")
            elif token == 'S': # Shadow: Перемещает верхнюю "мысль" из "сознания" в "подсознание"
                self.assembly_code.append("    dec edi") # Сдвигаем указатель сознания назад
                self.assembly_code.append("    mov al, byte [edi]") # Берем значение из сознания
                self.assembly_code.append("    inc esi") # Сдвигаем указатель подсознания вперед
                self.assembly_code.append("    mov byte [esi], al") # Помещаем значение в подсознание
            elif token == 'C': # Clarity: Перемещает верхнюю "мысль" из "подсознания" в "сознание"
                self.assembly_code.append("    dec esi") # Сдвигаем указатель подсознания назад
                self.assembly_code.append("    mov al, byte [esi]") # Берем значение из подсознания
                self.assembly_code.append("    inc edi") # Сдвигаем указатель сознания вперед
                self.assembly_code.append("    mov byte [edi], al") # Помещаем значение в сознание
            elif token == 'D': # Distort: (value XOR 0xAA) + 0x55
                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    mov al, byte [edi]")
                self.assembly_code.append("    xor al, 0xAA")
                self.assembly_code.append("    add al, 0x55")
                self.assembly_code.append("    mov byte [edi], al")
                self.assembly_code.append("    inc edi")
            elif token == 'E': # Echo: Дублирует верхнюю "мысль" в "сознании"
                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    mov al, byte [edi]")
                self.assembly_code.append("    inc edi")
                self.assembly_code.append("    mov byte [edi], al")
                self.assembly_code.append("    inc edi")
            elif token == 'V': # Void: Удаляет верхнюю "мысль" из "сознания"
                self.assembly_code.append("    dec edi")
            elif token == 'M': # Merge: (A XOR B) AND (A OR B)
                self.assembly_code.append("    dec edi") # B
                self.assembly_code.append("    mov bl, byte [edi]")
                self.assembly_code.append("    dec edi") # A
                self.assembly_code.append("    mov al, byte [edi]")
                self.assembly_code.append("    xor bh, bl") # bh = A XOR B
                self.assembly_code.append("    or cl, bl") # cl = A OR B
                self.assembly_code.append("    and bh, cl") # (A XOR B) AND (A OR B)
                self.assembly_code.append("    mov byte [edi], bh")
                self.assembly_code.append("    inc edi")
            elif token == 'P': # Print: Выводит верхнюю "мысль" из "сознания" как символ
                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    mov eax, 4")    # sys_write
                self.assembly_code.append("    mov ebx, 1")    # stdout
                self.assembly_code.append("    mov ecx, edi")  # адрес символа
                self.assembly_code.append("    mov edx, 1")    # длина
                self.assembly_code.append("    int 0x80")
                self.assembly_code.append("    inc edi") # Возвращаем указатель на место
            elif token == 'I': # Input: Считывает символ и помещает его ASCII-значение
                self.assembly_code.append("    mov eax, 3")    # sys_read
                self.assembly_code.append("    mov ebx, 0")    # stdin
                self.assembly_code.append("    mov ecx, edi")  # адрес для записи
                self.assembly_code.append("    mov edx, 1")    # длина
                self.assembly_code.append("    int 0x80")
                self.assembly_code.append("    inc edi") # Увеличиваем указатель стека после ввода
            elif token == 'L': # Loop: Если верхняя "мысль" в "сознании" равна нулю, переходит к K
                label_start = self._generate_label()
                label_end = self._generate_label()
                self.loop_stack.append((label_start, label_end))
                self.assembly_code.append(f"{label_start}:")
                self.assembly_code.append("    dec edi") # Смотрим на верхний элемент стека
                self.assembly_code.append("    cmp byte [edi], 0")
                self.assembly_code.append(f"    je {label_end}")
                self.assembly_code.append("    inc edi") # Возвращаем указатель
            elif token == 'K': # Kloop: Если верхняя "мысль" в "сознании" не равна нулю, переходит к L
                label_start, label_end = self.loop_stack.pop()
                self.assembly_code.append("    dec edi") # Смотрим на верхний элемент стека
                self.assembly_code.append("    cmp byte [edi], 0")
                self.assembly_code.append(f"    jne {label_start}")
                self.assembly_code.append("    inc edi") # Возвращаем указатель
                self.assembly_code.append(f"{label_end}:")

        self.assembly_code.append("    mov eax, 1") # sys_exit
        self.assembly_code.append("    xor ebx, ebx") # exit code 0
        self.assembly_code.append("    int 0x80")

        return "\n".join(self.assembly_code)

if __name__ == "__main__":
    test_tokens = ['F', 'S', 'C', 'D', 'E', 'V', 'M', 'P', 'I', 'L', 'K']
    codegen = CodeGenerator()
    asm_code = codegen.generate(test_tokens)
    print(asm_code)