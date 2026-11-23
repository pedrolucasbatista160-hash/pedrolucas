a = float(input('lado A:'))
b = float(input('lado B:'))
c = float(input('lado C:'))

if (a + b > c) and (a + c > b) and (b + c > b):
    if a == b == c:
        tipo = 'equilatero'
    elif a == b or a == c or b == c:
        tipo = 'isosceles'
    else:
        tipo = 'escaleno'
    print(f'Os lados formam um triângulo {tipo}.')