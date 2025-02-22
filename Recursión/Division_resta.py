def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"  
    if a < b:
        return 0 
    return 1 + division(a - b, b)  


dividendo = 15
divisor = 8
resultado = division(dividendo, divisor)
print(f"{dividendo} dividido entre {divisor} es {resultado}")