def sumar_lista(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sumar_lista(arr, n - 1)

numeros = [15, 8, 10, 2, 7, 9]  
resultado = sumar_lista(numeros, len(numeros))
print(f"Suma de la lista: {resultado}")