import sys
from ting_file_management.queue import Queue
import os  # Módulo os


#
def process(path_file: str, instance: Queue):  # Função process
    if any(item['nome_do_arquivo'] == path_file for item in instance.items):
        print(f'Arquivo {path_file} já processado anteriormente.')
        return
#

    if os.path.isfile(path_file):  # Verifica arquivo
        with open(path_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]  # Lê linhas
    else:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')  # Erro
        return
#

    file_info = {  # Informações do arquivo
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }
#

    instance.enqueue(file_info)  # Adiciona na fila
    print('Dados processados')
    print(file_info)  # Imprime informações
#


def remove(instance: Queue):
    if not instance.items:  # Verifica se a fila está vazia
        print('Não há elementos')
        return

    path_file = instance.items[0]['nome_do_arquivo']
    instance.dequeue()  # Remove o primeiro item da fila
    print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    try:
        file = instance.items[position]
        print(file)
    except IndexError:
        sys.stderr.write('Posição inválida\n')
