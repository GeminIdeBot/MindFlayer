import random

class AsmObfuscator:
    def __init__(self):
        pass

    def obfuscate(self, asm_code_lines):
        obfuscated_code = []
        for line in asm_code_lines:
            obfuscated_code.append(line)
            if random.random() < 0.2: # 20% шанс добавить обфускацию
                obfuscated_code.extend(self._add_random_nops())
                obfuscated_code.extend(self._add_random_register_ops())
        return obfuscated_code

    def _add_random_nops(self):
        num_nops = random.randint(1, 3)
        return ["    nop"] * num_nops

    def _add_random_register_ops(self):
        registers = ["eax", "ebx", "ecx", "edx"]
        random.shuffle(registers)
        ops = []
        for reg in registers[:random.randint(1, 2)]: # Выбираем 1-2 случайных регистра
            ops.append(f"    push {reg}")
            ops.append(f"    pop {reg}")
        return ops

if __name__ == "__main__":
    test_code = ["    mov eax, 1", "    int 0x80"]
    obfuscator = AsmObfuscator()
    obfuscated_asm = obfuscator.obfuscate(test_code)
    for line in obfuscated_asm:
        print(line)