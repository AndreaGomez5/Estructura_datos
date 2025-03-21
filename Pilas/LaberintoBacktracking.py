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

        while pila:
            x, y = pila[-1]

            if (x, y) == self.salida:
                return pila  