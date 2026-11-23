frase = input("Digite uma frase: ").lower()
vogais_lista = "aeiouáéíóúâêîôûãõ"

vogais = 0
consoantes = 0

for char in frase:
    if char.isalpha():  # Ignora espaços, números e pontuações
        if char in vogais_lista:
            vogais += 1
        else:
            consoantes += 1

print(f"Vogais: {vogais} | Consoantes: {consoantes}")