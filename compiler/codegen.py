import random

class CodeGenerator:
    def __init__(self):
        self.assembly_code = []
        self.data_segment = []
        self.label_counter = 0
        self.loop_stack = [] # Стек для хранения меток циклов

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
            if token == 'F': # Flicker - Мерцание
                self.assembly_code.append(f"    mov byte [edi], {random.randint(0, 255)}")
                self.assembly_code.append("    inc edi")
                if random.random() < 0.25: # Побочный эффект: 25% меняет местами две случайные "мысли" в "подсознании"
                    rand_offset1 = random.randint(0, 29999)
                    rand_offset2 = random.randint(0, 29999)
                    self.assembly_code.append(f"    mov al, byte [esi + {rand_offset1}]")
                    self.assembly_code.append(f"    mov bl, byte [esi + {rand_offset2}]")
                    self.assembly_code.append(f"    mov byte [esi + {rand_offset1}], bl")
                    self.assembly_code.append(f"    mov byte [esi + {rand_offset2}], al")
                if random.random() < 0.10: # Побочный эффект: 10% инвертирует биты *всех* "мыслей" в "сознании"
                    label_invert_start = self._generate_label()
                    label_invert_end = self._generate_label()
                    self.assembly_code.append(f"    mov ecx, edi") # Сохраняем текущий указатель сознания
                    self.assembly_code.append(f"    mov edx, mem") # Начинаем с начала сознания
                    self.assembly_code.append(f"{label_invert_start}:")
                    self.assembly_code.append(f"    cmp edx, ecx")
                    self.assembly_code.append(f"    jge {label_invert_end}")
                    self.assembly_code.append(f"    not byte [edx]")
                    self.assembly_code.append(f"    inc edx")
                    self.assembly_code.append(f"    jmp {label_invert_start}")
                    self.assembly_code.append(f"{label_invert_end}:")
            elif token == 'S': # Shift - Сдвиг
                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    mov al, byte [edi]")
                self.assembly_code.append("    inc esi")
                self.assembly_code.append("    mov byte [esi], al")
                if random.random() < 0.30: # Побочный эффект: 30% перемещает *случайную* "мысль" из "подсознания" обратно в "сознание"
                    rand_offset = random.randint(0, 29999)
                    self.assembly_code.append(f"    mov al, byte [esi + {rand_offset}]")
                    self.assembly_code.append("    inc edi")
                    self.assembly_code.append("    mov byte [edi], al")
            elif token == 'C': # Contort - Искажение
                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    mov al, byte [edi]")
                self.assembly_code.append("    mov bl, 5")
                self.assembly_code.append("    mul bl") # al = al * 5
                self.assembly_code.append("    xor al, 0x77")
                self.assembly_code.append("    mov bl, byte [edi]")
                self.assembly_code.append("    and bl, 0x11")
                self.assembly_code.append("    add al, bl")
                self.assembly_code.append("    mov byte [edi], al")
                self.assembly_code.append("    inc edi")
                if random.random() < 0.15: # Побочный эффект: 15% дублирует верхнюю "мысль" в "подсознании"
                    self.assembly_code.append("    dec esi")
                    self.assembly_code.append("    mov al, byte [esi]")
                    self.assembly_code.append("    inc esi")
                    self.assembly_code.append("    mov byte [esi], al")
                    self.assembly_code.append("    inc esi")
            elif token == 'D': # Disorient - Дезориентация
                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    mov al, byte [edi]")
                self.assembly_code.append("    test al, 1") # Проверяем четность
                label_even = self._generate_label()
                label_odd = self._generate_label()
                label_end_disorient = self._generate_label()
                self.assembly_code.append(f"    jz {label_even}") # Если четное
                self.assembly_code.append(f"    jmp {label_odd}") # Если нечетное

                self.assembly_code.append(f"{label_even}:") # Четное
                self.assembly_code.append("    mov bl, byte [edi-1]") # Меняем местами текущую и предыдущую
                self.assembly_code.append("    mov cl, byte [edi]")
                self.assembly_code.append("    mov byte [edi-1], cl")
                self.assembly_code.append("    mov byte [edi], bl")
                self.assembly_code.append(f"    jmp {label_end_disorient}")

                self.assembly_code.append(f"{label_odd}:") # Нечетное
                rand_offset = random.randint(0, 29999)
                self.assembly_code.append(f"    mov byte [esi + {rand_offset}], 0") # Обнуляем случайную "мысль" в "подсознании"
                self.assembly_code.append(f"    jmp {label_end_disorient}")

                self.assembly_code.append(f"{label_end_disorient}:")
                self.assembly_code.append("    inc edi")
            elif token == 'E': # Entangle - Запутывание
                self.assembly_code.append("    dec edi") # B
                self.assembly_code.append("    mov bl, byte [edi]")
                self.assembly_code.append("    dec edi") # A
                self.assembly_code.append("    mov al, byte [edi]")

                # A = (A OR B) - (A XOR B)
                self.assembly_code.append("    mov cl, al")
                self.assembly_code.append("    or cl, bl") # cl = A OR B
                self.assembly_code.append("    mov dh, al")
                self.assembly_code.append("    xor dh, bl") # dh = A XOR B
                self.assembly_code.append("    sub cl, dh") # cl = (A OR B) - (A XOR B)
                self.assembly_code.append("    mov byte [edi], cl") # Сохраняем результат в A

                # B = (A AND B) + (A OR B)
                self.assembly_code.append("    mov cl, al")
                self.assembly_code.append("    and cl, bl") # cl = A AND B
                self.assembly_code.append("    mov dh, al")
                self.assembly_code.append("    or dh, bl") # dh = A OR B
                self.assembly_code.append("    add cl, dh") # cl = (A AND B) + (A OR B)
                self.assembly_code.append("    inc edi")
                self.assembly_code.append("    mov byte [edi], cl") # Сохраняем результат в B

                self.assembly_code.append("    inc edi") # Возвращаем указатель

                if random.random() < 0.50: # Побочный эффект: 50% помещает на стек случайное число
                    self.assembly_code.append(f"    mov byte [edi], {random.randint(0, 255)}")
                    self.assembly_code.append("    inc edi")
            elif token == 'V': # Vanish - Исчезновение
                self.assembly_code.append("    dec edi")
                if random.random() < 0.20: # Побочный эффект: 20% удаляет также верхнюю "мысль" из "подсознания"
                    self.assembly_code.append("    dec esi")
            elif token == 'M': # Meld - Сплав
                self.assembly_code.append("    dec edi") # B
                self.assembly_code.append("    mov bl, byte [edi]")
                self.assembly_code.append("    dec edi") # A
                self.assembly_code.append("    mov al, byte [edi]")

                # (A XOR B) + (A AND B) + (B OR A)
                self.assembly_code.append("    mov cl, al")
                self.assembly_code.append("    xor cl, bl") # cl = A XOR B
                self.assembly_code.append("    mov dh, al")
                self.assembly_code.append("    and dh, bl") # dh = A AND B
                self.assembly_code.append("    add cl, dh") # cl = (A XOR B) + (A AND B)
                self.assembly_code.append("    mov dh, bl")
                self.assembly_code.append("    or dh, al") # dh = B OR A
                self.assembly_code.append("    add cl, dh") # cl = (A XOR B) + (A AND B) + (B OR A)
                self.assembly_code.append("    mov byte [edi], cl")
                self.assembly_code.append("    inc edi")

                if random.random() < 0.30: # Побочный эффект: 30% меняет указатель "сознания" на случайное значение
                    self.assembly_code.append(f"    mov edi, mem + {random.randint(0, 29999)}")
            elif token == 'P': # Project - Проекция
                if random.random() < 0.10: # Побочный эффект: 10% инвертирует биты выведенного символа перед выводом
                    self.assembly_code.append("    dec edi")
                    self.assembly_code.append("    not byte [edi]")
                    self.assembly_code.append("    inc edi")

                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    mov eax, 4")    # sys_write
                self.assembly_code.append("    mov ebx, 1")    # stdout
                self.assembly_code.append("    mov ecx, edi")  # адрес символа
                self.assembly_code.append("    mov edx, 1")    # длина
                self.assembly_code.append("    int 0x80")
                self.assembly_code.append("    inc edi")
            elif token == 'I': # Imprint - Отпечаток
                self.assembly_code.append("    mov eax, 3")    # sys_read
                self.assembly_code.append("    mov ebx, 0")    # stdin
                self.assembly_code.append("    mov ecx, edi")  # адрес для записи
                self.assembly_code.append("    mov edx, 1")    # длина
                self.assembly_code.append("    int 0x80")
                self.assembly_code.append("    inc edi")
                if random.random() < 0.20: # Побочный эффект: 20% дублирует введенный символ в "подсознании"
                    self.assembly_code.append("    dec edi")
                    self.assembly_code.append("    mov al, byte [edi]")
                    self.assembly_code.append("    inc edi")
                    self.assembly_code.append("    inc esi")
                    self.assembly_code.append("    mov byte [esi], al")
            elif token == 'L': # Labyrinth - Лабиринт
                label_start = self._generate_label()
                label_end = self._generate_label()
                self.loop_stack.append((label_start, label_end))

                if random.random() < 0.05: # Побочный эффект: 5% меняет порядок всех "мыслей" в "сознании" на обратный
                    label_reverse_start = self._generate_label()
                    label_reverse_end = self._generate_label()
                    self.assembly_code.append(f"    mov ecx, edi") # Сохраняем текущий указатель сознания
                    self.assembly_code.append(f"    mov edx, mem") # Начало сознания
                    self.assembly_code.append(f"    mov ebx, edi") # Конец сознания (текущий указатель)
                    self.assembly_code.append(f"    dec ebx") # Указывает на последний элемент

                    self.assembly_code.append(f"{label_reverse_start}:")
                    self.assembly_code.append(f"    cmp edx, ebx")
                    self.assembly_code.append(f"    jge {label_reverse_end}")
                    self.assembly_code.append(f"    mov al, byte [edx]")
                    self.assembly_code.append(f"    mov cl, byte [ebx]")
                    self.assembly_code.append(f"    mov byte [edx], cl")
                    self.assembly_code.append(f"    mov byte [ebx], al")
                    self.assembly_code.append(f"    inc edx")
                    self.assembly_code.append(f"    dec ebx")
                    self.assembly_code.append(f"    jmp {label_reverse_start}")
                    self.assembly_code.append(f"{label_reverse_end}:")
                    self.assembly_code.append(f"    mov edi, ecx") # Восстанавливаем указатель сознания

                self.assembly_code.append(f"{label_start}:")
                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    cmp byte [edi], 0")
                self.assembly_code.append(f"    je {label_end}")
                self.assembly_code.append("    inc edi")
            elif token == 'K': # Key - Ключ
                label_start, label_end = self.loop_stack.pop()
                if random.random() < 0.10: # Побочный эффект: 10% обнуляет верхнюю "мысль" в "подсознании"
                    self.assembly_code.append("    dec esi")
                    self.assembly_code.append("    mov byte [esi], 0")
                    self.assembly_code.append("    inc esi")

                self.assembly_code.append("    dec edi")
                self.assembly_code.append("    cmp byte [edi], 0")
                self.assembly_code.append(f"    jne {label_start}")
                self.assembly_code.append("    inc edi")
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