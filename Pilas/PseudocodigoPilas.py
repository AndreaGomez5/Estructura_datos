class Pila:
    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []

    def push(self, item):
        """Agrega un elemento a la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el último elemento de la pila."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Error: La pila está vacía"

    def peek(self):
        """Devuelve el último elemento de la pila sin eliminarlo."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Error: La pila está vacía"

    def is_empty(self):
        """Retorna True si la pila está vacía, de lo contrario False."""
        return len(self.items) == 0

    def tamaño(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)
    

if __name__ == "__main__":
    pila = Pila()
    pila.push(1)
    pila.push(2)
    pila.push(3)
    print("Elemento en la cima:", pila.peek())  
    print("Eliminando:", pila.pop())  
    print("La pila está vacía?", pila.is_empty())  
    print("Tamaño de la pila:", pila.tamaño())  