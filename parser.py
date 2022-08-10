from lexical.symbol_table import *
from lexical.scanner_mgol import *
from syntactic.functions import *


class Parser_mgol:

    def __init__(self):
        self.pilha = ['EOF', 0]
        self.pilha_aux = []
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
        # lexema = token.lexema
        # action(lexema, state)

        # (1) Seja a o primeiro símbolo de w$;

        # (2) while { /*Repita indefinidamente*/
        i = 0

        while not(self.is_final):
            # (3) seja s o estado no topo da pilha; if self.state == self.pilha[0]
            if True:
                print(self.token_arr[i])
                action_res = ''
                action_res = action(self.state, self.token_arr[i].lexema)
                print(' --> action_res', action_res)
                # (4) if (ACTION [s,a] = shift t ) {
                if action_res[0] == "s":
                    print("S <-----")
                    self.state = int(action_res.replace("s", ""))
                    print(self.state)
                    # (5) empilha t na pilha;
                    # ...

                    # (6) seja a o próximo símbolo da entrada;
                    # ...

                # (7) }else if (ACTION [s,a] = reduce A-> β ) {
                elif action_res == "r":
                    print("R <-----")
                    self.state = int(action_res.replace("r", ""))
                    print(self.state)
                    # (8) desempilha símbolos | β | da pilha;
                    # ...

                    # (9) faça o estado t agora ser o topo da pilha;
                    # ...

                    # (10) empilhe GOTO[t,A] na pilha;
                    # ...

                    # (11) imprima a produção A-> β ;
                    # ...

                # (12) }else if (ACTION [s,a] = accept ) pare; /* a análise terminou*/
                elif action_res == "acc":
                    print("acc <-----")

                # (13) else chame uma rotina de recuperação do erro;
                else:
                    print("else <-----")
                    # ...
            if len(self.token_arr) == 10:
                self.is_final == True
                print("is_final True")

            i = i + 1

        print("fim while")


prs = Parser_mgol()
# prs.parser()

arr = [0, 1, 2, 3]
print(arr[0])
print(arr[-1])
