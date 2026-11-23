def cifra_cesar(texto: str, deslocamento: int, criptografar: bool = True) -> str:
    if not criptografar:
        deslocamento = -deslocamento

    resultado = []
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado.append(novo_char)
        else:
            resultado.append(char)
    return "".join(resultado)

msg = "Ataque ao amanhecer!"
cifrada = cifra_cesar(msg, 3)
print("Cifrada:", cifrada)
print("Original:", cifra_cesar(cifrada, 3, criptografar=False))