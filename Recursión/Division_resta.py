def division(a, b, contador=0):
    if a < b:
        return contador
    else:
        return division(a - b, b, contador + 1)

if __name__ == "__main__":
    dividendo = 20
    divisor = 4
    print(f"El cociente de {dividendo} dividido entre {divisor} es: {division(dividendo, divisor)}")
