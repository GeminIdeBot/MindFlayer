from .parser import Parser
from .codegen import CodeGenerator
import sys

def compile_code(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    parser = Parser(code)
    tokens = parser.parse()

    codegen = CodeGenerator()
    asm_code = codegen.generate(tokens)

    with open(output_file, 'w') as f:
        f.write(asm_code)

    print(f"Код успешно скомпилирован в {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python compiler.py <входной_файл.mf> <выходной_файл.asm>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    compile_code(input_file, output_file)