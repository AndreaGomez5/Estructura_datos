def multiplicacion(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplicacion(a, b - 1)

if __name__ == "__main__":
    print(multiplicacion(16, 32))  
    print(multiplicacion(9, 12)) 
