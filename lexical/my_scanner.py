import os
from transitions import *
from symbol_table import Symbol_table
from my_token import my_Token


class my_Scanner:

    def __init__(self, text_file):
        self.codigo_fonte = []
        self.current_state = "q0"
        self.last_state = "q0"
        self.current_token = ""
        self.elements_print: my_Token = []
        self.read_text(text_file)

    def pertence_alfabeto(self, symbol):
        if(symbol in alfabeto):
            return True
        else:
            return False

    def read_text(self, text_file):
        script_dir = os.path.dirname(__file__)
        abs_file_path = script_dir + '\\' + text_file
        abs_file_path = abs_file_path.replace('\\', '/')
        with open(abs_file_path) as f:
            lines = f.readlines()
        for line in lines:
            self.codigo_fonte.append(line.replace("\n", ""))
        return self.codigo_fonte

    def scanner(self):
        for index_line, line in enumerate(self.codigo_fonte):
            self.current_state = "q0"
            self.last_state = "q0"
            self.current_token = ""

            # print current line
            # print(f"Line ({index_line}) --> {line} ")

            for index_char, char in enumerate(line):
                if(self.pertence_alfabeto(char) == False):
                    print("==> ERROR Linha: {} Coluna: {} => Caracter {} não pertence ao alfabeto".format(
                        index_line + 1, index_char + 1, char))

                # if(char == "\\" and line[index_char+1] == "n"):
                #     if(line[index_char-1] != '"' or line[index_char-1] != '{'):
                #         print(line[index_char-1])
                #         print(line[index_char])
                #         print(line[index_char+1])
                # Vendo futur_state
                if(funcao_de_transicao(self.current_state, char) == "q14"):
                    classe, tipo, isFinal = define_classe_tipo(
                        self.current_state)
                    if(isFinal == True):
                        token = my_Token(
                            self.current_token.lstrip(), classe, tipo)
                        token_from_table = table.insert_table(token)
                        if(classe != "COMENTARIO"):
                            self.elements_print.append(token_from_table)
                        self.current_token = ""
                        self.current_state = "q0"
                    else:
                        print("==> ERROR Linha: {} Coluna: {} => O estado {} não é final".format(
                            index_line + 1, index_char + 1, self.current_state))

                self.current_token += char
                # print current column
                # print(
                #     f"Column ({index_char}) --> state: {self.current_state} | last_state: {self.last_state} | char: {char}")
                self.last_state = self.current_state
                self.current_state = funcao_de_transicao(
                    self.current_state, char)

                if(index_char == len(line)-1):
                    classe, tipo, isFinal = define_classe_tipo(
                        self.current_state)
                    if(isFinal == True):
                        token = my_Token(
                            self.current_token.lstrip(), classe, tipo)
                        token_from_table = table.insert_table(token)
                        self.elements_print.append(token_from_table)
                        self.current_token = ""
                        self.current_state = "q0"
                    else:
                        print("==> ERROR Linha: {} Coluna: {} => O estado {} não é final".format(
                            index_line + 1, index_char + 1, self.current_state))

        # Adiciona End Of File
        final_token = my_Token("EOF", "EOF", None)
        final_token_from_table = table.insert_table(final_token)
        self.elements_print.append(final_token_from_table)


table = Symbol_table()

test_scanner = my_Scanner("test.txt")
print("========================================================")
print("================ INICIANDO SCANNER =====================")
print("========================================================")
test_scanner.scanner()

# table.get_table()

print("Elements_print:")
for item in test_scanner.elements_print:
    print(item)
