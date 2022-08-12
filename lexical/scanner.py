import os
from .transitions import *
from .symbol_table import Symbol_table
from .token import Token_mgol


class Scanner_mgol:

    def __init__(self, text_file):
        self.codigo_fonte = []
        self.current_state = "q0"
        self.last_state = "q0"
        self.current_lexema = ""
        self.token_arr = []
        self.position_arr = []
        self.read_file(text_file)
        self.print_inicia_scanner()
        self.symbol_table = Symbol_table()

    def print_inicia_scanner(self):
        print("========================================================")
        print("================ INICIANDO SCANNER =====================")
        print("========================================================")

    def print_elements(self):
        print("Array Tokens:")
        for item in self.token_arr:
            print(item)

    def return_elements(self):
        return self.token_arr

    def return_position_arr(self):
        return self.position_arr

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

    def scanner(self):
        i_l = 0
        i_c = 0
        for index_line, line in enumerate(self.codigo_fonte):
            i_l = index_line
            self.current_state = "q0"
            self.last_state = "q0"
            self.current_lexema = ""

            for index_char, char in enumerate(line):
                i_c = index_char
                if(self.pertence_alfabeto(char) == False):
                    print("==> ERRO LEXICO Linha: {} Coluna: {} => Caracter {} não pertence ao alfabeto".format(
                        index_line + 1, index_char + 1, char))

                if(get_next_state(self.current_state, char) == "q14"):
                    classe, tipo, isFinal = define_classe_tipo(
                        self.current_state)
                    if(isFinal == True):
                        token = Token_mgol(
                            self.current_lexema.lstrip(), classe, tipo)
                        token_from_table = self.symbol_table.insert_table(
                            token)
                        if(classe != "COMENTARIO"):
                            # setattr(type(token_from_table),
                            #         "line", index_line + 1)
                            # setattr(type(token_from_table),
                            #         "column", index_char + 1)
                            # print('['+str(token_from_table.line) +
                            #       ','+str(token_from_table.column)+']')
                            self.token_arr.append(token_from_table)
                            self.position_arr.append(
                                tuple((index_line + 1, index_char + 1)))
                        self.current_lexema = ""
                        self.current_state = "q0"
                    else:
                        print("==> ERRO LEXICO Linha: {} Coluna: {} => {}".format(
                            index_line + 1, index_char + 1, define_erro(self.current_state)))

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
                        token_from_table = self.symbol_table.insert_table(
                            token)
                        if(classe != "COMENTARIO"):
                            # setattr(type(token_from_table),
                            #         "line", index_line + 1)
                            # setattr(type(token_from_table),
                            #         "column", index_char + 1)
                            # print('['+str(token_from_table.line) +
                            #       ','+str(token_from_table.column)+']')
                            self.token_arr.append(token_from_table)
                            self.position_arr.append(
                                tuple((index_line + 1, index_char + 1)))
                        self.current_lexema = ""
                        self.current_state = "q0"
                    else:
                        print("==> ERRO LEXICO Linha: {} Coluna: {} => {}".format(
                            index_line + 1, index_char + 1, define_erro(self.current_state)))

        # Adiciona End Of File
        final_token = Token_mgol("eof", "eof", None)
        self.position_arr.append(
            tuple((i_l + 1, i_c + 1)))
        # setattr(type(final_token),
        #         "line", i_l + 1)
        # setattr(type(final_token),
        #         "column", i_c + 1)
        # print('['+str(token_from_table.line) +
        #       ','+str(token_from_table.column)+']')
        self.token_arr.append(final_token)
