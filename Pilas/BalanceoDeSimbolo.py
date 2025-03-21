def verificar_balanceo(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for i, simbolo in enumerate(expresion):
        if simbolo in pares.values():
            pila.append((simbolo, i))
        elif simbolo in pares:
            if not pila or pila[-1][0] != pares[simbolo]:
                return f"Error en la posición {i}: {simbolo} inesperado"
            pila.pop()
    
    if pila:
        simbolo, pos = pila[-1]
        return f"Error: Falta cerrar {simbolo} en la posición {pos}"
    
    return "Expresión correctamente balanceada"

expresion = "{[()]}[()]"
print(verificar_balanceo(expresion))

expresion_erronea = "{[(])}"
print(verificar_balanceo(expresion_erronea))
