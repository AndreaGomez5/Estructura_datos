def sumar_lista(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sumar_lista(arr, n - 1)

numeros = [25, 13, 11, 52, 10, 15]  
resultado = sumar_lista(numeros, len(numeros))
print(f"Suma de la lista: {resultado}")