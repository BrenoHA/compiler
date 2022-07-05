import os


class my_Scanner:
    def read_text(self, text_file):
        script_dir = os.path.dirname(__file__)
        abs_file_path = script_dir + '\\' + text_file
        # print(abs_file_path)
        abs_file_path = abs_file_path.replace('\\', '/')
        # print(abs_file_path)
        with open(abs_file_path) as f:
            lines = f.readlines()
        countLine = 0
        for line in lines:
            countColumn = 0
            countLine += 1
            for char in line:
                countColumn += 1
                print(f'line {countLine}: {line}')
                print(f'char {countColumn}: {char}')
                # Chamar a função da tabela de transição de estados
                # Verificar se é erro, e dentro dele se é realmente erro ou um novo estado zero
                # Append na tabela de simbolos
                #

                # Adicionar EOF
        return lines


test_scanner = my_Scanner()
test_scanner.read_text("test.txt")
