import string

def contar_palavras(texto: str) -> dict:
    # Remove pontuações e converte para minúsculo
    tabela = str.maketrans("", "", string.punctuation)
    palavras = texto.translate(tabela).lower().split()

    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia

paragrafo = "Python é incrível. Aprender Python abre muitas portas!"
print(contar_palavras(paragrafo))