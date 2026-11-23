def mesclar_estoques(estoque1: dict, estoque2: dict) -> dict:
    resultado = estoque1.copy()
    for produto, qtd in estoque2.items():
        resultado[produto] = resultado.get(produto, 0) + qtd
    return resultado

e1 = {'maçã': 10, 'banana': 5}
e2 = {'banana': 3, 'uva': 8}
print(mesclar_estoques(e1, e2))