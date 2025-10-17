import sys
from compiler.compiler import compile_code

def main():
    if len(sys.argv) != 3:
        print("Использование: python main.py <входной_файл.mf> <выходной_файл.asm>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    compile_code(input_file, output_file)

if __name__ == "__main__":
    main()