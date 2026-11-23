import random

def merge_sort(lista: list) -> list:
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return intercalar(esquerda, direita)

def intercalar(esq: list, dir: list) -> list:
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def busca_binaria(lista: list, alvo: int) -> int:
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Teste com 1.000 números
dados = [random.randint(1, 5000) for _ in range(1000)]
alvo_teste = dados[42]

dados_ordenados = merge_sort(dados)
indice = busca_binaria(dados_ordenados, alvo_teste)

print(f"Número {alvo_teste} encontrado no índice {indice} da lista ordenada.")
