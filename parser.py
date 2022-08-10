from lexical.symbol_table import *
from lexical.scanner_mgol import *


class Parser_mgol:

    def __init__(self):
        self.pilha = [0]
        self.pilha_aux = []
        self.state = self.pilha[-1]
        self.my_scanner = Scanner_mgol("test.txt")
        self.my_scanner.scanner()
        self.tokenArr = self.my_scanner.return_elements()
        self.isFinal = False

    def print_inicia_parser(self):
        print("========================================================")
        print("================= INICIANDO PARSER =====================")
        print("========================================================")

    def parser(self, token):
        self.print_inicia_parser()
        print(">PARSER")
        # lexema = token.lexema
        # action(lexema, state)

        # (1) Seja a o primeiro símbolo de w$;

        # (2) while { /*Repita indefinidamente*/
        while not(self.isFinal):

            # (3) seja s o estado no topo da pilha;
            if self.state == self.pilha[x]:

                # (4) if (ACTION [s,a] = shift t ) {
                if action(self.stlexema)[0] == "S":
                    print("ok")
                    # (5) empilha t na pilha;
                    # ...

                    # (6) seja a o próximo símbolo da entrada;
                    # ...

                # (7) }else if (ACTION [s,a] = reduce A-> β ) {
                elif action(self.state, lexema)[0] == "R":
                    print("ok")
                    # (8) desempilha símbolos | β | da pilha;
                    # ...

                    # (9) faça o estado t agora ser o topo da pilha;
                    # ...

                    # (10) empilhe GOTO[t,A] na pilha;
                    # ...

                    # (11) imprima a produção A-> β ;
                    # ...

                # (12) }else if (ACTION [s,a] = accept ) pare; /* a análise terminou*/
                elif action(self.state, lexema) == "acc":
                    print("ok")

                # (13) else chame uma rotina de recuperação do erro;
                else:
                    print("ok")
                    # ...


prs = Parser_mgol()
print(len(prs.tokenArr))
print(prs.tokenArr[1])

prs.parser("a")
