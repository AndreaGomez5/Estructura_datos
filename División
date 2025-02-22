def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    resultado = 0
    es_negativo = (a < 0) != (b < 0)  # El resultado será negativo si solo uno de los números es negativo

    a, b = abs(a), abs(b)  # Trabajar con valores absolutos

    while a >= b:  # Restar b de a hasta que a sea menor que b
        a -= b
        resultado += 1

    return -resultado if es_negativo else resultado  # Aplicar el signo correcto

# Ejemplo de uso
num1 = int(input("Ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))
print(f"Resultado: {dividir(num1, num2)}")