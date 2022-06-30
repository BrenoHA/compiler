from token import Token


class Symbol_table:
    def __init__(self):
        self.table = []
        self.set_reserved_keywords()

    def set_reserved_keywords(self):
        self.table.append(Token("inicio", "inicio", "inicio"))
        self.table.append(Token("varinicio", "varinicio", "varinicio"))
        self.table.append(Token("varfim", "varfim", "varfim"))
        self.table.append(Token("escreva", "escreva", "escreva"))
        self.table.append(Token("leia", "leia", "leia"))
        self.table.append(Token("se", "se", "se"))
        self.table.append(Token("entao", "entao", "entao"))
        self.table.append(Token("fimse", "fimse", "fimse"))
        self.table.append(Token("Repita", "Repita", "Repita"))
        self.table.append(Token("fimRepita", "fimRepita", "fimRepita"))
        self.table.append(Token("fim", "fim", "fim"))
        self.table.append(Token("inteiro", "inteiro", "inteiro"))
        self.table.append(Token("literal", "literal", "literal"))
        self.table.append(Token("real", "real", "real"))

    def get_table(self):
        print('Tabela de Simbolos:')
        for item in self.table:
            print(' -> {}, {}, {}'.format(item.classe, item.lexema, item.tipo))


t = Symbol_table()
t.get_table()


# a. Armazenará, EXCLUSIVAMENTE, tokens ID (reconhecidos pelo scanner) e palavras reservadas da linguagem.
# b. Cada item da tabela será um nó do tipo TOKEN como definido no item 1.
# c. As operações a serem realizadas para manipulação da Tabela de Símbolos são: Inserção, Busca e Atualização.
# d. Estruturas de dados, disponíveis em bibliotecas da linguagem escolhida, podem ser utilizadas.
# e. Ao iniciar o programa, a tabela de símbolos deverá ser preenchida automaticamente com todas as
#    PALAVRAS RESERVAS da linguagem. Essas estão disponíveis na TABELA 2. Para cada uma das
#    palavras reservadas, os campos classe, lexema e tipo serão todos preenchidos com a própria palavra.
#    Exemplo: Seja a palavra “se”, uma palavra reservada da linguagem, seu token conterá os seguintes
#    campos: lexema: if, classe: if, tipo: if
