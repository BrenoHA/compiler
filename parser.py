import copy
from lexical.symbol_table import *
from lexical.scanner import *
from syntactic.functions import *
from syntactic.grammarRules import *


class Parser_mgol:

    def __init__(self):
        self.pilha = [0]
        self.state = self.pilha[-1]
        self.my_scanner = Scanner_mgol("test.txt")
        self.my_scanner.scanner()
        self.token_arr = self.my_scanner.return_elements()
        self.position_arr = self.my_scanner.return_position_arr()
        self.index_token = 0
        self.is_final = False

    def print_inicia_parser(self):
        print("========================================================")
        print("================= INICIANDO PARSER =====================")
        print("========================================================")

    def print_error(self, n_error, state, token, position):
        row_error = df_action.iloc[n_error]
        available_classes = list(df_action.columns[1:])
        expected_classes = []
        for index_value, value in enumerate(row_error):
            if value != df_action[token.classe][state]:
                expected_classes.append(available_classes[index_value])
        # available_list = list(available)
        print("==> ERRO SINTATICO Estado:{} Linha: {} Coluna: {} Recebeu: ['{}'] Esperado: {}".format(
            state, position[0], position[1], token.classe, expected_classes))

    def outra_recuperação(self):
        print('o')

    def panic(self, token_arr):
        while self.index_token < (len(token_arr) - 1):
            pilha_aux = copy.deepcopy(self.pilha)
            while len(pilha_aux) > 0:
                acao = action(
                    pilha_aux[-1], token_arr[self.index_token].classe)
                if (acao[0]) != "e":
                    self.pilha = copy.deepcopy(pilha_aux)
                    return
                pilha_aux.pop()
            self.index_token += 1
        return

def single_shift(n_error):
    shift_counter = 0
    row_error = df_action.iloc[n_error]
    for value in row_error:
        if str(value)[0] == 's':
            shift_counter += 1
    # if(shift_counter == 1):

    def parser(self):
        self.print_inicia_parser()

        while not(self.is_final):
            self.state = self.pilha[-1]
            action_res = ''
            action_res = action(
                self.state, self.token_arr[self.index_token].classe)

            if action_res[0] == "s":
                self.state = int(action_res.replace("s", ""))
                self.pilha.append(self.state)
                self.index_token += 1

            elif action_res[0] == "r":
                self.state = int(action_res.replace("r", ""))
                grammar_rule = grammar_rules[self.state]
                grammar_sep = grammar_rule.split(' ')
                grammar_head = grammar_sep[0]
                grammar_body = grammar_sep[2:len(grammar_sep)]

                for index_body in range(0, len(grammar_body)):
                    self.pilha.pop()

                self.state = self.pilha[-1]
                goto_res = goto(
                    self.state, grammar_head)
                self.state = goto_res
                self.pilha.append(self.state)

                print(grammar_rule)

            elif action_res == "acc":
                print("ACC <-----")
                self.is_final = True

            else:
                n_error = int(action_res.replace("e", ""))
                self.print_error(
                    n_error, self.state, self.token_arr[self.index_token], self.position_arr[self.index_token])

                self.panic(self.token_arr)

            # Chamar uma segunda rotina de recuperação (tirar ; por ex)


prs = Parser_mgol()
prs.parser()
