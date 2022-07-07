class my_Token:
    def __init__(self, lexema, classe,  tipo):
        self.lexema = lexema
        self.classe = classe
        self.tipo = tipo

    # Print token
    def __str__(self):
        return ' --> Lexema: {} | Classe: {} | Tipo: {}'.format(self.lexema, self.classe, self.tipo)

    def set_token(self, lexema, classe,  tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo


# - Lexema: armazenará a palavra computada;
# - Classe: armazenará a classificação do lexema reconhecido;
# - Tipo: armazenará o tipo de dado do lexema quando for possível determiná-lo. Em caso de
# constantes numéricas ou literais, preencher com inteiro, real ou literal. Os demais casos, preencher
# com NULO

# 'Token:{{\n Lexema: {}\n Classe: {}\n Tipo: {}\n }}'.format(self.lexema, self.classe, self.tipo)
