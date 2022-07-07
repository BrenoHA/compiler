from ast import Num
from lib2to3.pgen2.grammar import opmap
from ssl import OP_NO_RENEGOTIATION
from typing import Literal
from utils.guidelines import *


def funcao_de_transicao(state, symbol):

    if state == "q0":
        if symbol == " ":
            return "q0"
        elif symbol in digitos:
            return "q1"
        elif symbol == '"':
            return "q2"
        elif symbol in letras:
            return "q3"
        elif symbol == "{":
            return "q4"
        elif symbol == "EOF":  # fim
            return "q5"
        elif symbol == ">":
            return "q6"
        elif symbol == "=":
            return "q7"
        elif symbol == "<":
            return "q8"
        elif symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            return "q9"
        elif symbol == "(":
            return "q10"
        elif symbol == ")":
            return "q11"
        elif symbol == ";":
            return "q12"
        elif symbol == ",":
            return "q13"
        else:
            return "q14"

    elif state == "q1":
        if symbol in digitos:
            return "q1"
        elif symbol == ".":
            return "q1_1"
        elif symbol == "E" or symbol == "e":  # ?
            return "q1_3"
        else:
            return "q14"

    elif state == "q1_1":
        if symbol in digitos:
            return "q1_2"
        else:
            return "q14"

    elif state == "q1_2":
        if symbol in digitos:
            return "q1_2"
        elif symbol == "E" or symbol == "e":
            return "q1_6"
        else:
            return "q14"

    elif state == "q1_6":
        if symbol in digitos:
            return "q1_8"
        elif symbol == "+" or symbol == "-":
            return "q1_7"
        else:
            return "q14"

    elif state == "q1_7":
        if symbol in digitos:
            return "q1_8"
        else:
            return "q14"

    elif state == "q1_8":
        if symbol in digitos:
            return "q1_8"
        else:
            return "q14"

    elif state == "q2":
        if symbol in alfabeto:
            return "q2"
        elif symbol == '"':
            return "q2_1"
        else:
            return "q14"

    # if state == "q2_1": Do Nothing

    elif state == "q3":
        if symbol in letras or symbol in digitos or symbol == '_':
            return "q3"
        else:
            return "q14"

    elif state == "q4":
        if symbol in alfabeto:
            return "q4"
        elif symbol == "":
            return "q4_1"
        else:
            return "q14"

    # if state == "q5": Do Nothing

    elif state == "q6":
        if symbol == "=":
            return "q7"
        else:
            return "q14"

    # if state == "q7": Do Nothing

    elif state == "q8":
        if symbol == ">" or symbol == "=":
            return "q7"
        elif symbol == "-":
            return "q8_1"
        else:
            return "q14"

    # if state == "q9": Do Nothing

    # if state == "q10": Do Nothing

    # if state == "q11": Do Nothing

    # if state == "q12": Do Nothing

    # if state == "q13": Do Nothing

    else:
        return "q14"


def define_classe_tipo(state):
    classe = None
    tipo = None
    isFinal = True
    if state == "q1" or state == "q1_5":
        classe = "NUM"
        tipo = "inteiro"
    elif state == "q1_2" or state == "q1_8":
        classe = "NUM"
        tipo = "real"
    elif state == "q2_1":
        classe = "LIT"
        tipo = "literal"
    elif state == "q3":
        classe = "ID"
    elif state == "q4_1":
        classe = "COMENTARIO"
    elif state == "q5":
        classe = "EOF"
    elif state == "q6" or state == "q7" or state == "q8":
        classe = "OPR"
    elif state == "q8_1":
        classe = "RCB"
    elif state == "q9":
        classe = "OPM"
    elif state == "q10":
        classe = "AB_P"
    elif state == "q11":
        classe = "FC_P"
    elif state == "q12":
        classe = "PT_V"
    elif state == "q13":
        classe = "VIR"
    elif state == "q14":
        classe = "ERRO"
    else:
        isFinal = False

    return classe, tipo, isFinal


# print(funcao_de_transicao("q0", "{"))
# print(funcao_de_transicao("q0", "["))
# print(funcao_de_transicao("q0", "%"))
print(define_classe_tipo("q8_1"))
