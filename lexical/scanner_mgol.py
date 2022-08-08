import os
from .transitions import *
from .symbol_table import Symbol_table
from .token_mgol import Token_mgol


class Scanner_mgol:

    def __init__(self, text_file):
        self.codigo_fonte = []
        self.current_state = "q0"
        self.last_state = "q0"
        self.current_lexema = ""
        self.elements_print: Token_mgol = []
        self.read_file(text_file)
        self.print_inicia_scanner()

    def print_inicia_scanner(self):
        print("========================================================")
        print("================ INICIANDO SCANNER =====================")
        print("========================================================")

    def print_elements(self):
        print("Elements_print:")
        for item in self.elements_print:
            print(item)

    def pertence_alfabeto(self, symbol):
        if(symbol in alfabeto):
            return True
        else:
            return False

    def read_file(self, text_file):
        script_dir = os.path.dirname(__file__)
        abs_file_path = script_dir + '\\' + text_file
        abs_file_path = abs_file_path.replace('\\', '/')
        with open(abs_file_path) as f:
            lines = f.readlines()
        for line in lines:
            self.codigo_fonte.append(line.replace("\n", ""))
        return self.codigo_fonte

    def scanner(self, table,init_line,init_char):
        for index_line, line in enumerate(self.codigo_fonte[init_line:]):
            self.current_state = "q0"
            self.last_state = "q0"
            self.current_lexema = ""

            for index_char, char in enumerate(line[init_char:]):
                if(self.pertence_alfabeto(char) == False):
                    print("==> ERROR Linha: {} Coluna: {} => Caracter {} não pertence ao alfabeto".format(
                        index_line + 1, index_char + 1, char))

                if(get_next_state(self.current_state, char) == "q14"):
                    classe, tipo, isFinal = define_classe_tipo(
                        self.current_state)
                    if(isFinal == True):
                        token = Token_mgol(
                            self.current_lexema.lstrip(), classe, tipo)
                        token_from_table = table.insert_table(token)
                        self.current_lexema = ""
                        self.current_state = "q0"
                        if(classe != "COMENTARIO"):
                            self.elements_print.append(token_from_table)
                            return token,init_line+index_line,init_char+index_char
                    else:
                        print("==> ERROR Linha: {} Coluna: {} =>  ".format(
                            index_line + 1, index_char + 1)+ define_erro(self.current_state) )

                self.current_lexema += char
                self.last_state = self.current_state
                self.current_state = get_next_state(
                    self.current_state, char)

                if(index_char == len(line)-1):
                    classe, tipo, isFinal = define_classe_tipo(
                        self.current_state)
                    if(isFinal == True):
                        token = Token_mgol(
                            self.current_lexema.lstrip(), classe, tipo)
                        token_from_table = table.insert_table(token)
                        self.current_lexema = ""
                        self.current_state = "q0"
                        if(classe != "COMENTARIO"):
                            self.elements_print.append(token_from_table)
                            return token,init_line+index_line,init_char+index_char

                    else:
                        print("==> ERROR Linha: {} Coluna: {} => ".format(
                            index_line + 1, index_char + 1)+ define_erro(self.current_state) )

        # Adiciona End Of File
        final_token = Token_mgol("EOF", "EOF", None)
        self.elements_print.append(final_token)
