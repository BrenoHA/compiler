
class Parser_mgol:

    def __init__(self):
        self.pilha = [0]
        self.pilha_aux = []
        self.state = self.pilha[-1]
        self.print_inicia_parser()

    def print_inicia_parser(self):
        print("========================================================")
        print("================= INICIANDO PARSER =====================")
        print("========================================================")

    def parser(self, token):
        print(">PARSER")
        # lexema = token.lexema
        # action(lexema, state)


parser = Parser_mgol()
parser.parser("a")
