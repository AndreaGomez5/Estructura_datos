def multiplicar(a, b):
    resultado = 0
    es_negativo = (a < 0) != (b < 0)  # El resultado será negativo si solo uno de los números es negativo

    a, b = abs(a), abs(b)  # Trabajar con valores absolutos

    for _ in range(b):  # Sumar 'a', 'b' veces
        resultado += a

    return -resultado if es_negativo else resultado  # Aplicar el signo correcto

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Resultado: {multiplicar(num1, num2)}")