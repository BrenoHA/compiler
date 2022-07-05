from ast import Num
from lib2to3.pgen2.grammar import opmap
from ssl import OP_NO_RENEGOTIATION
from typing import Literal
from utils.guidelines import *


# q0 estado inicial
# q1 num_final
# q1_1 num
# q1_2 num_final
# q1_3 num
# q1_4 num
# q1_5 num_final
# q1_6 num
# q1_7 num
# q1_8 num_final
# q2 lit
# q2_1 lit_final
# q3 id_final
# q4 comentario
# q4_1 comentario_final
# q5 eof_final
# q6 opr_final
# q7 opr_final
# q8 opr_final
# q8_1 rcb_final
# q9 opm_final
# q10 ab_p_final
# q11 fc_p_final
# q12 pt_v_final
# q13 vir_final
# q14 erro


def pertence_alfabeto(symbol):
    if(symbol in alfabeto):
        return True
    else:
        return False


def funcao_de_transicao(state, symbol):
    print('ok')
    if(pertence_alfabeto(symbol) == False):
        return "ERRO: Caracter não pertence ao alfabeto"

    if state == "q0":
        if symbol in digitos:
            return "q1"
        elif symbol == '"':
            return "q2"
        elif symbol in letras or digitos or '_':
            return "q3"
        elif symbol == "{":
            return "q4"
        elif symbol == "EOF":  # fim
            return "q5"
        elif symbol == "<":
            return "q6"
        elif symbol == "=":
            return "q7"
        elif symbol == ">":
            return "q8"
        elif symbol == "+" or "-" or "*" or "/":
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

    if state == "q1":
        if symbol in digitos:
            return "q1"
        elif symbol == ".":  # \.
            return "q1_1"
        elif symbol == "E" or "e":
            return "q1_3"
        else:
            return "q14"

    if state == "q1_1":
        if symbol in digitos:
            return "q1_2"
        else:
            return "q14"

    if state == "q1_2":
        if symbol in digitos:
            return "q1_2"
        elif symbol == "E" or "e":
            return "q1_6"
        else:
            return "q14"

    if state == "q1_6":
        if symbol in digitos:
            return "q1_8"
        elif symbol == "+" or "-":
            return "q1_7"
        else:
            return "q14"

    if state == "q1_7":
        if symbol in digitos:
            return "q1_8"
        else:
            return "q14"

    if state == "q1_8":
        if symbol in digitos:
            return "q1_8"
        else:
            return "q14"

    if state == "q2":
        if symbol == ".":
            return "q2"
        elif symbol == '"':
            return "q2_1"
        else:
            return "q14"

    # if state == "q2_1": Do Nothing

    if state == "q3":
        if symbol in letras or digitos or '_':
            return "q3"
        else:
            return "q14"

    if state == "q4":
        if symbol == ".":
            return "q4"
        elif symbol == "":
            return "q4_1"
        else:
            return "q14"

    # if state == "q5": Do Nothing

    if state == "q6":
        if symbol == "=":
            return "q7"
        else:
            return "q14"

    # if state == "q7": Do Nothing

    if state == "q8":
        if symbol == ">" or "=":
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
