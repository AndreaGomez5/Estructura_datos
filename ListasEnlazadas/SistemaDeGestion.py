from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        self.siguiente = None
    
    def __str__(self):
        return f"[{self.prioridad}] {self.descripcion} - Vence: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class ListaTareas:
    def __init__(self):
        self.cabeza = None
    
    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        
        if not self.cabeza or (nueva_tarea.prioridad < self.cabeza.prioridad or 
                               (nueva_tarea.prioridad == self.cabeza.prioridad and nueva_tarea.fecha_vencimiento < self.cabeza.fecha_vencimiento)):
            nueva_tarea.siguiente = self.cabeza
            self.cabeza = nueva_tarea
            return
        
        actual = self.cabeza
        while actual.siguiente and (actual.siguiente.prioridad < nueva_tarea.prioridad or 
                                   (actual.siguiente.prioridad == nueva_tarea.prioridad and actual.siguiente.fecha_vencimiento < nueva_tarea.fecha_vencimiento)):
            actual = actual.siguiente
        
        nueva_tarea.siguiente = actual.siguiente
        actual.siguiente = nueva_tarea
    
    def eliminar_tarea(self, descripcion):
        actual = self.cabeza
        anterior = None
        
        while actual:
            if actual.descripcion == descripcion:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Tarea eliminada: {descripcion}")
                return
            anterior = actual
            actual = actual.siguiente
        print("Tarea no encontrada.")
    
    def mostrar_tareas(self):
        if not self.cabeza:
            print("No hay tareas registradas.")
            return
        
        actual = self.cabeza
        print("\nLista de Tareas:")
        while actual:
            print(actual)
            actual = actual.siguiente
    
    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                print("Tarea encontrada:", actual)
                return
            actual = actual.siguiente
        print("Tarea no encontrada.")
    
    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)
        print(f"Tarea '{descripcion}' marcada como completada y eliminada de la lista.")

tareas = ListaTareas()
tareas.agregar_tarea("Terminar proyecto", 1, "2024-03-20")
tareas.agregar_tarea("Comprar comida", 2, "2024-03-15")
tareas.agregar_tarea("Hacer ejercicio", 3, "2024-03-18")

tareas.mostrar_tareas()
tareas.buscar_tarea("Comprar comida")
tareas.marcar_completada("Comprar comida")
tareas.mostrar_tareas()