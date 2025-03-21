def resolver_laberinto(laberinto, inicio, fin):
    filas, columnas = len(laberinto), len(laberinto[0])
    pila = [inicio]  
    visitado = set()
    
    movimientos = [(0,1), (1,0), (0,-1), (-1,0)]  
    while pila:
        x, y = pila[-1]  
        
        if (x, y) == fin:
            return pila 
        
        if (x, y) not in visitado:
            visitado.add((x, y))

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 0 and (nx, ny) not in visitado:
                pila.append((nx, ny))
                break
        else:
            pila.pop()  

    return None  

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
fin = (4, 4)
solucion = resolver_laberinto(laberinto, inicio, fin)

print("Ruta encontrada:", solucion)
