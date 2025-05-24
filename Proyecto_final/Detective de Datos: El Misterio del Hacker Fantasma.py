import random
import time
import hashlib

class NodoServidor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.hackeado = False 

class ColaEventos:
    def __init__(self):
        self.eventos = []

    def encolar(self, evento):
        self.eventos.append(evento)

    def desencolar(self):
        return self.eventos.pop(0) if self.eventos else None

    def esta_vacia(self):
        return len(self.eventos) == 0

class ArbolEvidencia:
    def __init__(self, dato, izquierda=None, derecha=None):
        self.dato = dato
        self.izquierda = izquierda
        self.derecha = derecha

    def imprimir(self, nivel=0):
        if self.derecha:
            self.derecha.imprimir(nivel + 1)
        print("    " * nivel + f"🔍 {self.dato}")
        if self.izquierda:
            self.izquierda.imprimir(nivel + 1)

class DetectiveDigital:
    def __init__(self):
        self.servidores = self.crear_red()
        self.eventos = ColaEventos()
        self.ruta_correcta = ["A", "C", "D"]
        self.evidencia = self.generar_arbol_evidencia()
        self.vidas = 3
        self.puntuacion = 0
        self.tiempo_total = 120  

    def crear_red(self):
        nombres = ["A", "B", "C", "D", "E"]
        cabeza = NodoServidor(nombres[0])
        actual = cabeza
        for nombre in nombres[1:]:
            nuevo = NodoServidor(nombre)
            actual.siguiente = nuevo
            actual = nuevo
        return cabeza

    def generar_arbol_evidencia(self):
        return ArbolEvidencia("IP sospechosa",
            izquierda=ArbolEvidencia("Correo filtrado"),
            derecha=ArbolEvidencia("Acceso remoto",
                izquierda=ArbolEvidencia("VPN privada"),
                derecha=ArbolEvidencia("Archivo cifrado")
            )
        )

    def mostrar_ruta(self):
        print("\n🌐 Red de servidores:")
        actual = self.servidores
        while actual:
            print(f" -> Servidor {actual.nombre} (Hackeado: {'Sí' if actual.hackeado else 'No'})", end="")
            actual = actual.siguiente
        print()

    def analizar_eventos(self):
        print("\n📡 Analizando eventos de red...")
        eventos_posibles = [
            "Ping inusual", "Conexión segura detectada", "Paquete dañado",
            "Error 404 en el servidor", "Conexión fallida", "Posible hacker detectado"
        ]
        for _ in range(3):
            tiempo = random.randint(1, 3)
            time.sleep(tiempo)
            evento = random.choice(eventos_posibles)
            self.eventos.encolar(evento)
            print(f" + Evento registrado: {evento} ({tiempo}s)")

    def hackear_servidor(self, servidor):
        """Simula el hackeo de un servidor, el jugador debe repararlo para detener el hacker."""
        if random.choice([True, False]):
            servidor.hackeado = True
            print(f"⚠️ ¡El servidor {servidor.nombre} ha sido hackeado!")
        else:
            print(f"💻 El servidor {servidor.nombre} está seguro por ahora.")

    def reparar_servidor(self, servidor):
        """El jugador puede intentar reparar un servidor hackeado."""
        print(f"\n🔧 Intentando reparar el servidor {servidor.nombre}...")
        tiempo_reparacion = random.randint(5, 10)
        print(f"⏳ Tiempo estimado para reparación: {tiempo_reparacion} segundos...")
        time.sleep(tiempo_reparacion)
        exito = random.choice([True, False])
        if exito:
            servidor.hackeado = False
            print(f"✅ El servidor {servidor.nombre} ha sido reparado con éxito.")
            self.puntuacion += 15 
        else:
            print(f"❌ No lograste reparar el servidor {servidor.nombre} a tiempo.")
            self.puntuacion -= 10  

    def generar_contraseña(self):
        """Genera una contraseña aleatoria para los servidores hackeados."""
        return hashlib.sha256(str(random.randint(1000, 9999)).encode()).hexdigest()[:6]

    def resolver_contraseña(self):
        """Simula la solución de una contraseña para el hacker."""
        print("\n🧩 Resuelve la contraseña del servidor hackeado.")
        respuesta = self.generar_contraseña()
        intentos = 3
        while intentos > 0:
            intento_usuario = input(f"Ingresa la contraseña ({intentos} intentos restantes): ")
            if intento_usuario == respuesta:
                print("✅ ¡Contraseña correcta! El servidor ha sido desbloqueado.")
                self.puntuacion += 20 
                return True
            else:
                print("❌ Contraseña incorrecta.")
                intentos -= 1
        print(f"❌ ¡La contraseña correcta era {respuesta}!")
        self.puntuacion -= 15  
        return False

    def investigar(self):
        print("\n🕵️ Revisando evidencia:")
        self.evidencia.imprimir()

        decision = input("\n¿Seguir la pista izquierda o derecha? (i/d): ").lower()
        if decision == "d":
            print("📁 Abriste un archivo cifrado... ¡pista correcta!")
            self.puntuacion += 10
        else:
            print("⚠️ La pista era una trampa... pérdida de tiempo.")
            self.puntuacion -= 5

    def resolver_misterio(self):
        print("\n🔍 Rastrea la ruta del hacker. Elige 3 servidores (ej. A B C):")
        eleccion = input(">> ").upper().split()
        if eleccion == self.ruta_correcta:
            print("\n✅ ¡Ruta correcta! Has atrapado al hacker fantasma.")
            self.puntuacion += 50  
            return True
        else:
            print("\n❌ Ruta equivocada. El hacker escapó... por ahora.")
            self.vidas -= 1
            return False

    def jugar(self):
        print("🎮 Bienvenido a 'Detective de Datos: El Misterio del Hacker Fantasma'")
        start_time = time.time()
        while True:
            if self.vidas <= 0 or time.time() - start_time > self.tiempo_total:
                print("\n😢 Has perdido todas tus vidas o se acabó el tiempo. El hacker ha escapado...")
                break

            print(f"\n💡 Vidas restantes: {self.vidas} | Puntuación: {self.puntuacion} | Tiempo restante: {max(0, self.tiempo_total - int(time.time() - start_time))} segundos")
            self.mostrar_ruta()
            self.analizar_eventos()

            actual = self.servidores
            while actual:
                if random.random() < 0.2: 
                    self.hackear_servidor(actual)
                actual = actual.siguiente

            reparar = input("\n¿Quieres intentar reparar algún servidor hackeado? (s/n): ").lower()
            if reparar == "s":
                servidor_reparar = input("Elige el servidor a reparar (A, B, C, D, E): ").upper()
                actual = self.servidores
                while actual:
                    if actual.nombre == servidor_reparar and actual.hackeado:
                        self.reparar_servidor(actual)
                        break
                    actual = actual.siguiente

            self.investigar()

            if self.resolver_misterio():
                print("\n🔓 ¡Felicidades, atrapaste al hacker!")
            else:
                print("\n😢 El hacker escapó esta vez.")

            jugar_otra = input("\n¿Quieres volver a jugar? (s/n): ").lower()
            if jugar_otra != "s":
                print(f"¡Gracias por jugar! Tu puntuación final es: {self.puntuacion}")
                break

if __name__ == "__main__":
    juego = DetectiveDigital()
    juego.jugar()