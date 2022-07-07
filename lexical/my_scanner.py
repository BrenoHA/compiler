import os
from transitions import *
from symbol_table import *
from my_token import my_Token


class my_Scanner:

    def __init__(self, text_file):
        self.codigo_fonte = []
        self.current_state = "q0"
        self.last_state = "q0"
        self.current_token = ""
        self.elements_print: my_Token = []
        self.read_text(text_file)

    def get_codigo_fonte(self):  # ?
        return self.codigo_fonte

    def pertence_alfabeto(self, symbol):
        if(symbol in alfabeto):
            return True
        else:
            return False

    def read_text(self, text_file):
        script_dir = os.path.dirname(__file__)
        abs_file_path = script_dir + '\\' + text_file
        # print(abs_file_path)
        abs_file_path = abs_file_path.replace('\\', '/')
        # print(abs_file_path)
        with open(abs_file_path) as f:
            lines = f.readlines()
        countLine = 0
        for line in lines:
            countColumn = 0
            countLine += 1
            # print(f'line {countLine}: {line}')
            self.codigo_fonte.append(line.replace("\n", ""))
            # TODO NÃO PODE RETIRAR ESPAÇO ASSIM
            for char in line:
                countColumn += 1
                # print(f'char {countColumn}: {char}')
        return self.codigo_fonte

    def scanner(self):
        total_lines = len(self.codigo_fonte)
        for index_line, line in enumerate(self.codigo_fonte):
            self.current_state = "q0"
            self.last_state = "q0"
            self.current_token = ""

            print(f"Line ({index_line}) --> {line} ")

            for index_char, char in enumerate(line):
                if(self.pertence_alfabeto(char) == False):
                    print("ERROR Linha: {} Coluna: {} => Caracter {} não pertence ao alfabeto".format(
                        index_line + 1, index_char + 1, char))
                    raise SystemExit

                # Vendo futur_state
                if(funcao_de_transicao(self.current_state, char) == "q14"):
                    classe, tipo, isFinal = define_classe_tipo(
                        self.current_state)
                    if(isFinal == True):
                        if(funcao_de_transicao(self.current_state, char) == "q14"):
                            token = my_Token(self.current_token, classe, tipo)
                            token_from_table = table.insert_table(token)
                            self.elements_print.append(token_from_table)
                            self.current_token = ""
                            self.current_state = "q0"
                    else:
                        print("ERROR Linha: {} Coluna: {} => O estado {} não é final".format(
                            index_line + 1, index_char + 1, self.current_state))
                        raise SystemExit

                self.current_token += char
                print(
                    f"Column ({index_char}) --> state: {self.current_state} | last_state: {self.last_state} | char: {char}")
                self.last_state = self.current_state
                self.current_state = funcao_de_transicao(
                    self.current_state, char)
        # Adiciona final do arquivo
        final_token = my_Token("EOF", "EOF", None)
        final_token_from_table = table.insert_table(final_token)
        self.elements_print.append(final_token_from_table)


table = Symbol_table()

test_scanner = my_Scanner("test.txt")
# print(test_scanner.get_codigo_fonte())
print("========================================================")
print("========================================================")
test_scanner.scanner()

table.get_tokens()

table.get_table()


print("elements_print:")
for item in test_scanner.elements_print:
    print(item)
