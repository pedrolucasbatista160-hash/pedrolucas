def remover_duplicatas(lista: list) -> list:
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos

numeros = [1, 2, 2, 3, 4, 4, 5, 1]
print(remover_duplicatas(numeros))