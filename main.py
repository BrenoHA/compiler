from lexical.symbol_table import *
from lexical.scanner_mgol import *


def main():
    symbol_table = Symbol_table()
    test_scanner = Scanner_mgol("test.txt")
    test_scanner.scanner(symbol_table)
    test_scanner.print_elements()


main()
