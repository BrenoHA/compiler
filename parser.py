from lexical.symbol_table import *
from lexical.scanner import *
from syntactic.functions import *
from syntactic.grammarRules import *
from syntactic.functions import *

class Parser_mgol:

    def __init__(self):
        self.pilha_aux = []
        self.pilha = ['EOF', 0]
        # (1) Seja a o primeiro símbolo de w$;
        self.state = self.pilha[-1]
        self.my_scanner = Scanner_mgol("test.txt")
        self.my_scanner.scanner()
        self.token_arr = self.my_scanner.return_elements()
        self.is_final = False

    def print_inicia_parser(self):
        print("========================================================")
        print("================= INICIANDO PARSER =====================")
        print("========================================================")

    def parser(self):
        self.print_inicia_parser()

        index_token = 0

        # (2) while { /*Repita indefinidamente*/
        while not(self.is_final):
            # (3) seja s o estado no topo da pilha; if self.state == self.pilha[0]
            self.state = self.pilha[-1]
            # print(self.token_arr[index_token])
            action_res = ''
            action_res = action(
                self.state, self.token_arr[index_token].classe)
            # print(' --> action_res', action_res)
            # (4) if (ACTION [s,a] = shift t ) {
            if action_res[0] == "s":
                self.state = int(action_res.replace("s", ""))
                # (5) empilha t na pilha;
                self.pilha.append(self.state)
                # print(self.pilha)

                # (6) seja a o próximo símbolo da entrada;
                index_token = index_token + 1

            # (7) }else if (ACTION [s,a] = reduce A-> β ) {
            elif action_res[0] == "r":
                self.state = int(action_res.replace("r", ""))
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
                # print(' --> goto_res', goto_res)

                # (10) empilhe GOTO[t,A] na pilha;
                self.state = goto_res
                self.pilha.append(self.state)

                # (11) imprima a produção A-> β ;
                print(grammar_rule)

            # (12) }else if (ACTION [s,a] = accept ) pare; /* a análise terminou*/
            elif action_res == "acc":
                print("ACEITACAO <-----")
                self.is_final = True

            # (13) else chame uma rotina de recuperação do erro;
            else:
                print("ELSE <-----")
                # Printar o erro
                error_translation(df_action, self.state,self.token_arr[index_token].classe)
                break
            
            # Chamar uma rotina de recuperação ( PANIC )

            # Chamar uma segunda rotina de recuperação (tirar ; por ex)


prs = Parser_mgol()
prs.parser()
