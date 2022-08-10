from lexical.symbol_table import *
from lexical.scanner_mgol import *


def main():

    test_scanner = Scanner_mgol("test.txt")
    test_scanner.scanner()
    test_scanner.print_elements()
    tokenArr = test_scanner.return_elements()
    print(len(tokenArr))
    print(tokenArr[1])


main()
