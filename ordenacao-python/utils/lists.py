import random

def gerar_lista(tam: int, tipo: str) -> list[int]:
    """
    Gera uma lista de inteiros de acordo com um tipo especificado.

    Args:
        tam (int): O tamanho da lista a ser gerada.
        tipo (str): O tipo de lista a ser gerada.
                    Aceita 'crescente', 'decrescente' ou 'random'.

    Returns:
        list[int]: A lista de inteiros gerada.

    Raises:
        ValueError: Se o tipo especificado for inválido.
    """
    if tipo == 'crescente':
        return list(range(tam))
    elif tipo == 'decrescente':
        return list(range(tam - 1, -1, -1))
    elif tipo == 'random':
        lista = list(range(tam))
        random.shuffle(lista)
        return lista
    else:
        raise ValueError("Tipo inválido. Use 'crescente', 'decrescente' ou 'random'.")