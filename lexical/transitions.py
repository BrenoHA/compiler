from .utils.guidelines import *


def get_next_state(state, symbol):

    if state == "q0":
        if symbol == " ":
            return "q0"
        elif symbol == '"':
            return "q2"
        elif symbol == "{":
            return "q4"
        elif symbol == "eof":  # fim
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
        elif symbol in digitos:
            return "q1"
        elif symbol in letras:
            return "q3"
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
        if symbol == '"':
            return "q2_1"
        elif symbol in alfabeto:
            return "q2"
        else:
            return "q14"

    # if state == "q2_1": Do Nothing

    elif state == "q3":
        if symbol in letras or symbol in digitos or symbol == '_':
            return "q3"
        else:
            return "q14"

    elif state == "q4":
        if symbol == "}":
            return "q4_1"
        elif symbol in alfabeto:
            return "q4"
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
        classe = "num"
        tipo = "inteiro"
    elif state == "q1_2" or state == "q1_8":
        classe = "num"
        tipo = "real"
    elif state == "q2_1":
        classe = "lit"
        tipo = "literal"
    elif state == "q3":
        classe = "id"
    elif state == "q4_1":
        classe = "comentario"
    elif state == "q5":
        classe = "eof"
    elif state == "q6" or state == "q7" or state == "q8":
        classe = "opr"
    elif state == "q8_1":
        classe = "rcb"
    elif state == "q9":
        classe = "opm"
    elif state == "q10":
        classe = "ab_p"
    elif state == "q11":
        classe = "fc_p"
    elif state == "q12":
        classe = "pt_v"
    elif state == "q13":
        classe = "vir"
    elif state == "q14":
        classe = "ERRO"
    else:
        isFinal = False

    return classe, tipo, isFinal


def define_erro(state):
    if state == "q1_1":
        return "Float mal formado"
    elif state == ("q1_3" or "q1_4" or "q1_6" or "q1_7"):
        return "Notacao cientifica mal formada"
    elif state == "q2":
        return "Falta fechar aspas"
    elif state == "q4":
        return "Falta fechar chaves"
