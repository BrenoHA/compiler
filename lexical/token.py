class Token_mgol:
    def __init__(self, lexema, classe,  tipo):
        self.lexema = lexema
        self.classe = classe
        self.tipo = tipo

    # Print token
    # def __str__(self):
    #     return ' --> Lexema: {} | Classe: {} | Tipo: {}'.format(self.lexema, self.classe, self.tipo)

    def set_token(self, lexema, classe,  tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo
