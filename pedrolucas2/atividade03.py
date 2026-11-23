num = int (input('digite um número inteiro:'))

paridade = 'par' if num % 2 == 0 else 'impar'

if num > 0:
    sinal = 'positivo'
elif num < 0:
    sinal = 'negativo'
else:
    sinal = 'zero (neutro)'

print(f'O número {num} é {paridade} e {sinal}.')

