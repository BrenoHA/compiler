from ast import Num
from lib2to3.pgen2.grammar import opmap
from ssl import OP_NO_RENEGOTIATION
from typing import Literal
from util.grammar import *

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



def funcao_de_transicao(state, symbol):
    if state[0] == "q0":
        if symbol in numbers_dict:
            return ["q1", "num_final"]
        elif symbol == '"':
            return ["q2", "num"]
        elif symbol in letras:
            return ["q3", "id_final"]
        elif symbol == "{":
            return ["q4", "comentario"]
        elif symbol == "fim":
            return ["q5", "eof_final"]
        elif symbol == "<":
            return ["q6", "opr_final"]
        elif symbol == "=":
            return ["q7", "opr_final"]
        elif symbol == ">":
            return ["q8", "opr_final"]
        elif symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            return ["q9", "opm_final"]
        elif symbol == "(":
            return ["q10", "ab_p_final"]
        elif symbol == ")":
            return ["q11", "fc_p_final"]
        elif symbol == ";":
            return ["q12", "pt_v_final"]
        elif symbol == ",":
            return ["q13", "vir_final"]
        else:
            return ["Se", "2"]

    if state[0] =="q1":
        if symbol in numbers_dict:
            return ["q1", "num_final"]
        elif symbol == ".":
            return ["q1_1", "num"]
        elif symbol == "e" or symbol == "E":
            return ["q1_3", "Num"]
        else:
            return ["Se", "2"]

    if state[0] =="q1_1":
        if symbol in numbers_dict:
            return ["q1_2", "num_final"]
        else:
            return ["Se", "2"]

    if state[0] == "q1_2":
        if symbol in numbers_dict:
            return ["q1_2", "num_final"]
        elif symbol == "e" or symbol == "E":
            #q1_6 = s4
            return ["q1_6", "num"] 
        else:
            return ["Se", "2"]

    if state[0] == "q1_6":
        if symbol == "+" or symbol == "-":
            #q1_7 = s5
            return ["q1_7", "num"]
        if symbol in numbers_dict:
            #q1_8 = s6
            return["q1_8", "num_final"]
        else:
            return ["Se", "2"]

    if state[0] == "q1_7":
        if symbol in numbers_dict:
            return["q1_8", "num_final"]
        else:
            return ["Se", "2"]

    if state[0] == "q1_8":
        if symbol in numbers_dict:
            return ["q1_8", "num"]
        else:
            return ["Se", "2"]

    if state[0] == "q2":
        if symbol == '"':
            return ["q2_1", "lit_final"]
        else:
            return ["s8", "3"]

    if state[0] == "s8":
        if symbol == '"':
            return ["q2_1", "lit_final"]
        else:
            return ["s8", "3"]

    if state[0] ==  "Se" and state[1] == "1":
        return ["Se", "1"]

    if  state[0] == "Se" and state[1] == "2":
        return ["Se", "2"]

    if state[0] ==  "s9" or state[0] ==  "s13" or state[0] ==  "s14" or state[0] ==  "s17" or state[0] ==  "s18" or state[0] ==  "s19" or state[0] ==  "s20" or state[0] ==  "s21" or state[0] ==  "s22" or state[0] ==  "s23" or state[0] ==  "s24":
        return ["Se", "2"]

    if state[0] == "s10":
        if symbol in letras+numbers_dict or symbol == "_":
            return ["s10", "id"]
        else:
            return ["Se", "2"]

    if state[0] == "s11":
        if symbol == "}":
            return ["s13", "Comentário"]
        else:
            return ["s12", "4"]

    if state[0] == "s12":
        if symbol == "}":
            return ["s13", "Comentário"]
        else:
            return ["s12", "4"]

    if state[0] == "s15":
        if symbol == "=":
            return ["s21", "OPR"]
        elif symbol == ">":
            return ["s22", "OPR"]
        if symbol == "-":
            return ["s23", "RCB"]
        else:
            return ["Se", "2"]

    if state[0] == "s16":
        if symbol == "=":
            return ["s24", "OPR"]
        else:
            return ["Se", "2"]