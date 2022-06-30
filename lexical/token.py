class Token:
    def __init__(self, classe, lexema, tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def set_token(self, classe, lexema, tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def get_token(self):
        return 'Token:\n Classe: {}\n Lexema: {}\n Tipo: {}\n'.format(self.classe, self.lexema, self.tipo)


# - Classe: armazenará a classificação do lexema reconhecido;
# - Lexema: armazenará a palavra computada;
# - Tipo: armazenará o tipo de dado do lexema quando for possível determiná-lo. Em caso de
# constantes numéricas ou literais, preencher com inteiro, real ou literal. Os demais casos, preencher
# com NULO
