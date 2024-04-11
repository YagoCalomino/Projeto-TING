from ting_file_management.abstract_queue import AbstractQueue


# Definindo a classe Queue que herda de AbstractQueue

class Queue(AbstractQueue):  # Inicializando a fila
    def __init__(self):
        self.items = []
#

    def __len__(self):  # Retorna o tamanho da fila
        return len(self.items)
#

    def enqueue(self, value):  # Adiciona um elemento no final da fila
        self.items.append(value)
#

    def dequeue(self):  # Remove e retorna o primeiro elemento da fila
        if len(self.items) != 0:
            return self.items.pop(0)

        return None  # Se a fila estiver vazia, retorna None
#

    def search(self, index):  # Procura um elemento na fila pelo índice
        if not 0 <= index < len(self.items):  # Se o índice for inválido, lança uma exceção
            raise IndexError("Índice Inválido ou Inexistente")

        return self.items[index]  # Retorna o elemento no índice especificado
#
