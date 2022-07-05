from my_token import my_Token
from utils.guidelines import *


class Symbol_table:
    def __init__(self):
        self.table = []
        self.set_reserved_keywords()

    def set_reserved_keywords(self):
        for keyword in palavras_reservadas:
            self.table.append(my_Token(keyword, keyword, keyword))

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

    def insert_table(self, my_Token):
        print('Inserindo o Token(Lexema: {}, Classe: {}, Tipo: {} ):'.format(
            my_Token.lexema, my_Token.classe, my_Token.tipo))
        self.table.append(my_Token)

    def search_table(self, lexema):
        hasToken = False
        print('Procurando o Token com lexema: {}'.format(lexema))
        for item in self.table:
            if(item.lexema == lexema):
                hasToken = True
                print(' -> Lexema: {} | Classe: {} | Tipo: {}'.format(item.lexema,
                                                                      item.classe, item.tipo))
                return item
        if(hasToken == False):
            print('Token com lexema: "{}" não encontrado'.format(lexema))
            return None

    def update_table(self, old_lexema, new_lexema):
        print('Atualizando o Token com lexema: {}'.format(old_lexema))
        if(self.search_table(old_lexema) is None):
            return("Token não encontrado")
        else:
            old_token = self.search_table(old_lexema)
            old_token.lexema = new_lexema


t = Symbol_table()
test_token = my_Token("lexAaaa", "clasAa", "TipoA")
t.insert_table(test_token)
# t.update_table('class_lexema', 'new_class_lexema')
# t.get_table()
t.get_tokens()
# t.search_table("inicioo")


# a. Armazenará, EXCLUSIVAMENTE, tokens ID (reconhecidos pelo scanner) e palavras reservadas da linguagem.
# b. Cada item da tabela será um nó do tipo my_TOKEN como definido no item 1.
# c. As operações a serem realizadas para manipulação da Tabela de Símbolos são: Inserção, Busca e Atualização.
# d. Estruturas de dados, disponíveis em bibliotecas da linguagem escolhida, podem ser utilizadas.
# e. Ao iniciar o programa, a tabela de símbolos deverá ser preenchida automaticamente com todas as
#    PALAVRAS RESERVAS da linguagem. Essas estão disponíveis na TABELA 2. Para cada uma das
#    palavras reservadas, os campos classe, lexema e tipo serão todos preenchidos com a própria palavra.
#    Exemplo: Seja a palavra “se”, uma palavra reservada da linguagem, seu token conterá os seguintes
#    campos: lexema: if, classe: if, tipo: if
