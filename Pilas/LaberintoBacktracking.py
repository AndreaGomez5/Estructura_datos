class Laberinto:
    def __init__(self, laberinto, inicio, salida):
        self.laberinto = laberinto
        self.inicio = inicio
        self.salida = salida
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

    def resolver(self):
        pila = [self.inicio]
        visitados = set()
        visitados.add(self.inicio)

        while pila:
            x, y = pila[-1]  

            
            if (x, y) == self.salida:
                return pila  

            
            encontrado = False
            for dx, dy in self.movimientos:
                nx, ny = x + dx, y + dy

                
                if (0 <= nx < self.filas and 0 <= ny < self.columnas and 
                    self.laberinto[nx][ny] == 0 and (nx, ny) not in visitados):
                    
                    pila.append((nx, ny))  
                    visitados.add((nx, ny))
                    encontrado = True
                    break  

            
            if not encontrado:
                pila.pop()

        return None  

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
salida = (4, 4)


solver = Laberinto(laberinto, inicio, salida)
camino = solver.resolver()


if camino:
    print("Camino encontrado:", camino)
else:
    print("No hay solución para el laberinto.")