digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z",
          "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
demais_caracteres = [",", ";", ":", ".", "!", "?", "\\", "*",
                     "+", "-", "/", "(", ")", "{", "}", "[", "]", "<", ">", "=", "‘", "“"]
alfabeto = digitos + letras + demais_caracteres


class Alfabeto:
    def __init__(self):
        self.digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z",
                       "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
        self.demais_caracteres = [",", ";", ":", ".", "!", "?", "\\", "*",
                                  "+", "-", "/", "(", ")", "{", "}", "[", "]", "<", ">", "=", "‘", "“"]
        self.alfabelo = self.digitos + self.letras + self.demais_caracteres
