from my_token import my_Token
import os

class my_scanner:
    def read_text(self,text_file):
        script_dir = os.path.dirname(__file__)
        abs_file_path = script_dir + '\\' + text_file
        print(abs_file_path)
        abs_file_path = abs_file_path.replace('\\', '/')
        print(abs_file_path)
        with open(abs_file_path) as f:
            lines = f.readlines()
        count = 0
        for line in lines:
            count += 1
            print(f'line {count}: {line}') 
        return lines

# test_token = my_Token("classeb", "lexemabb", "tipoB")
# print(test_token.get_token())
test_scanner = my_scanner()
test_scanner.read_text("test_file.txt")
