import time
import matplotlib.pyplot as plt
from utils.lists import gerar_lista 
from utils.sorts import bubble_sort, selection_sort, insertion_sort

tamanhos = [10, 100, 500, 1000, 2000]

def medir_tempo(algoritmo, tipo_lista, nome_alg, nome_lista):
    """
    Mede o tempo de execução de um algoritmo de ordenação
    para diferentes tamanhos de lista.

    Args:
        algoritmo (callable): Função de ordenação.
        tipo_lista (str): O tipo de lista ('crescente', 'decrescente', 'random').
        nome_alg (str): Nome do algoritmo.
        nome_lista (str): Nome do tipo de lista para exibição.

    Returns:
        list[float]: Lista com tempos em segundos.
    """
    tempos = []
    for tam in tamanhos:
        lista = gerar_lista(tam, tipo_lista)
        
        tempoInicio = time.perf_counter()
        algoritmo(lista.copy())  # usa cópia para não modificar o original
        tempoFim = time.perf_counter() # perf_counter() tem mais precisão e é recomendado para benchmarks
        duracao = tempoFim - tempoInicio
        tempos.append(duracao)

        print(f"Tempo {nome_alg} - {nome_lista} (n={tam}): {duracao:.9f} s")

    return tempos

algoritmos = {
    "Bubble Sort (O(n²))": bubble_sort,
    "Selection Sort (O(n²))": selection_sort,
    "Insertion Sort (O(n²))": insertion_sort,
    "Python sorted() (O(n log n))": sorted
}

geradores = {
    "Crescente": "crescente",
    "Decrescente": "decrescente",
    "Aleatória": "random"
}

for nome_gerador, tipo_lista in geradores.items():
    print("-" * 50)
    print(f"Iniciando medições para listas do tipo: {nome_gerador}")
    print("-" * 50)

    plt.figure(figsize=(10, 7))

    for nome_alg, func_alg in algoritmos.items():
        tempos = medir_tempo(func_alg, tipo_lista, nome_alg, nome_gerador)   
        plt.plot(tamanhos, tempos, marker="o", linestyle="-", label=f"{nome_alg}")

    plt.title(f"Comparação de Algoritmos de Ordenação\n(Entrada: Lista {nome_gerador})")
    plt.xlabel("Tamanho da Lista (n)")
    plt.ylabel("Tempo de Execução (segundos)")
    plt.legend()
    plt.grid(axis='y', linestyle=':')
    plt.xticks(tamanhos)
    plt.show()