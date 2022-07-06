import os
from transitions import *


class my_Scanner:

    def __init__(self, text_file):
        self.codigo_fonte = []
        self.current_state = "q0"
        # self.current_symbol = ""
        self.read_text(text_file)

    def get_codigo_fonte(self):
        return self.codigo_fonte

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
            print(f'line {countLine}: {line}')
            self.codigo_fonte.append(line.replace("\n", "").replace(" ", ""))
            for char in line:
                countColumn += 1
                print(f'char {countColumn}: {char}')
        return self.codigo_fonte

    def scanner(self):
        for line in self.codigo_fonte:
            print("-- new line --")
            for char in line:
                print(f"state: {self.current_state} | char: {char}")
                self.current_state = funcao_de_transicao(
                    self.current_state, char)

    # Chamar a função da tabela de transição de estados
    # Verificar se é erro, e dentro dele se é realmente erro ou um novo estado zero
    # Append na tabela de simbolos
    #

    # Adicionar EOF


test_scanner = my_Scanner("test.txt")
# print(test_scanner.get_codigo_fonte())
print("========================================================")
print("========================================================")
test_scanner.scanner()
