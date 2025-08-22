def bubble_sort(lista: list[int]) -> None:
    """
    Ordena uma lista usando o algoritmo Bubble Sort.

    Args:
        lista (list[int]): Lista de inteiros a ser ordenada.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def selection_sort(lista: list[int]) -> None:
    """
    Ordena uma lista usando o algoritmo Selection Sort.

    Args:
        lista (list[int]): Lista de inteiros a ser ordenada.
    """
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]


def insertion_sort(lista: list[int]) -> None:
    """
    Ordena uma lista usando o algoritmo Insertion Sort.

    Args:
        lista (list[int]): Lista de inteiros a ser ordenada.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave