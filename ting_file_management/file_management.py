import sys
import os


def txt_importer(path_file):  # Definindo a função txt_importer
    if os.path.splitext(path_file)[1] != '.txt':
        sys.stderr.write('Formato inválido\n')  # Caso Seja Invalida
        return None  # Retorna None se a extensão for inválida

    if os.path.isfile(path_file):
        with open(path_file, 'r') as file:
            content = file.readlines()  # Lê todas as linhas do arquivo
        return [line.strip() for line in content]
    else:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        return None  # Retorna None se o arquivo não for encontrado
