def parenteses_validos(s: str) -> bool:
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pares.values():
            pilha.append(char)
        elif char in pares:
            if not pilha or pilha.pop() != pares[char]:
                return False

    return len(pilha) == 0

print(parenteses_validos("{[()]}"))  
print(parenteses_validos("{[(])}"))