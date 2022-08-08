from lexical.token_mgol import *
from lexical.scanner_mgol import *


def main():
    symbol_table = Symbol_table()
    test_scanner = Scanner_mgol("test.txt")
    text = test_scanner.codigo_fonte
    token = []
    current_line = 0
    current_char = 0
    while (current_line!=len(text) or current_char!=len(text[len(text)])):
        print(current_line,current_char)
        token,current_line,current_char = test_scanner.scanner(symbol_table,current_line,current_char)
        print(token)
    test_scanner.print_elements()


main()
