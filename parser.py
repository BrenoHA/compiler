from lexical.symbol_table import *
from lexical.scanner_mgol import *
from syntactic.functions import *
from syntactic.grammarRules import *


class Parser_mgol:

    def __init__(self):
        self.pilha = ['EOF', 0]
        self.pilha_aux = []
        # Seta o estado com o último elemento da pilha
        self.state = self.pilha[-1]
        self.my_scanner = Scanner_mgol("test.txt")
        self.my_scanner.scanner()
        self.token_arr = self.my_scanner.return_elements()
        # self.my_scanner.print_elements()
        self.is_final = False

    def print_inicia_parser(self):
        print("========================================================")
        print("================= INICIANDO PARSER =====================")
        print("========================================================")

    def parser(self):
        self.print_inicia_parser()
        print(">PARSER")

        # (1) Seja a o primeiro símbolo de w$;

        index_token = 0

        # (2) while { /*Repita indefinidamente*/
        while not(self.is_final):
            # (3) seja s o estado no topo da pilha; if self.state == self.pilha[0]
            self.state = self.pilha[-1]
            print(self.token_arr[index_token])
            action_res = ''
            action_res = action(
                self.state, self.token_arr[index_token].classe)
            print(' --> action_res', action_res)
            # (4) if (ACTION [s,a] = shift t ) {
            if action_res[0] == "s":
                print("S <-----")
                self.state = int(action_res.replace("s", ""))
                print(self.state)
                # (5) empilha t na pilha;
                self.pilha.append(self.state)
                print(self.pilha)

                # (6) seja a o próximo símbolo da entrada;
                index_token = index_token + 1

            # (7) }else if (ACTION [s,a] = reduce A-> β ) {
            elif action_res[0] == "r":
                print("R <-----")
                self.state = int(action_res.replace("r", ""))
                print(self.state)
                grammar_rule = grammar_rules[self.state]
                grammar_sep = grammar_rule.split(' ')
                grammar_head = grammar_sep[0]
                grammar_body = grammar_sep[2:len(grammar_sep)]

                for index_body in range(0, len(grammar_body)):
                    # (8) desempilha símbolos | β | da pilha;
                    self.pilha.pop()

                # (9) faça o estado t agora ser o topo da pilha;
                self.state = self.pilha[-1]

                goto_res = goto(
                    self.state, grammar_head)

                # (10) empilhe GOTO[t,A] na pilha;
                self.state = goto_res
                print(self.state)
                self.pilha.append(self.state)

                # (11) imprima a produção A-> β ;
                print('----------------------------------')
                print('----------> ', grammar_rule)
                print('----------------------------------')

            # (12) }else if (ACTION [s,a] = accept ) pare; /* a análise terminou*/
            elif action_res == "acc":
                print("acc <-----")
                break

            # (13) else chame uma rotina de recuperação do erro;
            else:
                print("else <-----")
                # ...

            # FINAL???
            if len(self.token_arr) == 10:
                self.is_final == True
                print("is_final True")

        print("fim while")


prs = Parser_mgol()
prs.parser()
