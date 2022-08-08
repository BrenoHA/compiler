from lexical.scanner_mgol import *

scanner = Scanner_mgol("test.txt")
example_file = scanner.codigo_fonte

def retornaToken(text_file,init_line, init_char):
    for index_line, line in enumerate(text_file[init_line:]):
        print("line: "+str(index_line)+"=>"+line)
        for index_char, char in enumerate(line[init_char:]):
            print("char: "+str(index_char)+"=>"+char)
            if(index_char==4):
                return init_line+index_line,init_char+index_char


current_line, current_char = retornaToken(example_file,0,0)
current_line, current_char = retornaToken(example_file,current_line,current_char)
current_line, current_char = retornaToken(example_file,current_line,current_char)




