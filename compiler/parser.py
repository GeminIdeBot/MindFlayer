class Parser:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.valid_tokens = ['F', 'S', 'C', 'D', 'E', 'V', 'M', 'P', 'I', 'L', 'K', '/', 'N', 'O']

    def parse(self):
        for char in self.code:
            if char in self.valid_tokens:
                self.tokens.append(char)
        return self.tokens

if __name__ == "__main__":
    test_code = "FSCD EVMP ILK"
    parser = Parser(test_code)
    parsed_tokens = parser.parse()
    print(f"Исходный код: {test_code}")
    print(f"Разобранные токены: {parsed_tokens}")