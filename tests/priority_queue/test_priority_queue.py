from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    mock = [{'qtd_linhas': 7}, {'qtd_linhas': 6}, {'qtd_linhas': 1},
            {'qtd_linhas': 2}, {'qtd_linhas': 3}, ]

    p_queue = PriorityQueue()

    # Enfileirar elementos em ordem diferente
    p_queue.enqueue(mock[0]), p_queue.enqueue(mock[4]),
    p_queue.enqueue(mock[3]), p_queue.enqueue(mock[2]),
    p_queue.enqueue(mock[1])
    assert len(p_queue) == 5

    # Pesquisar elementos em ordem diferente
    assert p_queue.search(1) == mock[0]
    assert p_queue.search(4) == mock[1]
    with pytest.raises(IndexError):
        p_queue.search(10)

    # Desenfileirar elementos em ordem diferente
    assert p_queue.dequeue() == mock[1]
    assert p_queue.dequeue() == mock[2]
    assert p_queue.dequeue() == mock[3]
    assert p_queue.dequeue() == mock[4]
    assert p_queue.dequeue() == mock[0]
    assert len(p_queue) == 0

    # Enfileirar elementos em ordem diferente
    p_queue.enqueue(mock[1])
    p_queue.enqueue(mock[0])
    assert len(p_queue) == 2
