from token_mgol import Token_mgol
from utils.guidelines import *


class Symbol_table:
    def __init__(self):
        self.table = []
        self.set_reserved_keywords()

    def set_reserved_keywords(self):
        for keyword in palavras_reservadas:
            self.table.append(Token_mgol(keyword, keyword, keyword))

    def get_table(self):
        print('Tabela de Simbolos:')
        for item in self.table:
            print(' -> Lexema: {} | Classe: {} | Tipo: {}'.format(item.lexema,
                                                                  item.classe, item.tipo))

    def get_tokens(self):
        print('Tokens:')
        for item in self.table:
            if(palavras_reservadas.count(item.lexema) == 0):
                print(' -> Lexema: {} | Classe: {} | Tipo: {}'.format(item.lexema,
                                                                      item.classe, item.tipo))

    def insert_table(self, Token_mgol):

        if(Token_mgol.lexema in palavras_reservadas):
            return self.search_table(Token_mgol.lexema)
        else:
            if(Token_mgol.classe == "ID"):
                if(not self.search_table(Token_mgol.lexema)):
                    # print('Inserindo o Token (Lexema: {}, Classe: {}, Tipo: {}):'.format(
                    #     Token_mgol.lexema, Token_mgol.classe, Token_mgol.tipo))
                    self.table.append(Token_mgol)
                return Token_mgol
            else:
                return Token_mgol

    def search_table(self, lexema):
        hasToken = False
        for item in self.table:
            if(item.lexema == lexema):
                hasToken = True
                # print(' -> Lexema: {} | Classe: {} | Tipo: {}'.format(item.lexema,
                #                                                       item.classe, item.tipo))
                return item
        if(hasToken == False):
            # print('Token com lexema: "{}" não encontrado'.format(lexema))
            return None

    def update_table(self, old_lexema, new_lexema):
        # print('Atualizando o Token com lexema: {}'.format(old_lexema))
        if(self.search_table(old_lexema) is None):
            return("O Token atual não foi encontrado")
        else:
            old_token = self.search_table(old_lexema)
            old_token.lexema = new_lexema
