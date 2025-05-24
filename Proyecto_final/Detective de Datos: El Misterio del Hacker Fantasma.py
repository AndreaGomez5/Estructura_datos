import random
import time
import hashlib
from sklearn.tree import DecisionTreeClassifier
import numpy as np

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
        self.ruta_correcta = random.sample(["A", "B", "C", "D", "E"], 3)
        self.evidencia = self.generar_arbol_evidencia()
        self.vidas = 3
        self.puntuacion = 0
        self.tiempo_total = 120
        self.modelo_ml = self.entrenar_modelo_hackeo()

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

    def entrenar_modelo_hackeo(self):
        # Entrenamos un modelo con datos simulados
        X = []
        y = []
        for _ in range(1000):
            hora = random.randint(0, 23)
            nombre = random.randint(0, 4)  # A=0, B=1, ...
            carga = random.randint(0, 100)
            hack = 1 if carga > 70 or (hora >= 22 or hora <= 3) else 0
            X.append([nombre, hora, carga])
            y.append(hack)
        modelo = DecisionTreeClassifier()
        modelo.fit(X, y)
        return modelo

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
            tiempo = random.randint(1, 2)
            time.sleep(tiempo)
            evento = random.choice(eventos_posibles)
            self.eventos.encolar(evento)
            print(f" + Evento registrado: {evento} ({tiempo}s)")

    def predecir_hackeo(self, nombre):
        hora = time.localtime().tm_hour
        indice = ord(nombre) - ord("A")
        carga = random.randint(0, 100)
        pred = self.modelo_ml.predict([[indice, hora, carga]])[0]
        return pred == 1

    def hackear_servidor(self, servidor):
        if self.predecir_hackeo(servidor.nombre):
            servidor.hackeado = True
            print(f"⚠️ ¡El servidor {servidor.nombre} ha sido hackeado! (Predicción ML)")
        else:
            print(f"💻 El servidor {servidor.nombre} está seguro.")

    def reparar_servidor(self, servidor):
        print(f"\n🔧 Intentando reparar el servidor {servidor.nombre}...")
        tiempo_reparacion = random.randint(5, 10)
        print(f"⏳ Tiempo estimado para reparación: {tiempo_reparacion} segundos...")
        time.sleep(tiempo_reparacion)
        exito = random.choice([True, False])
        if exito:
            servidor.hackeado = False
            print(f"✅ Reparación exitosa.")
            self.puntuacion += 15
        else:
            print("❌ Falló la reparación.")
            self.puntuacion -= 10

    def generar_contraseña(self):
        return hashlib.sha256(str(random.randint(1000, 9999)).encode()).hexdigest()[:6]

    def resolver_contraseña(self):
        print("\n🧩 Resuelve la contraseña del servidor hackeado.")
        respuesta = self.generar_contraseña()
        intentos = 3
        while intentos > 0:
            intento = input(f"Contraseña ({intentos} intentos): ")
            if intento == respuesta:
                print("✅ ¡Correcta!")
                self.puntuacion += 20
                return True
            else:
                print("❌ Incorrecta.")
                intentos -= 1
        print(f"❌ La correcta era: {respuesta}")
        self.puntuacion -= 15
        return False

    def investigar(self):
        print("\n🕵️ Revisando evidencia:")
        self.evidencia.imprimir()
        decision = input("\n¿Seguir la pista izquierda o derecha? (i/d): ").lower()
        if decision == "d":
            print("📁 Pista correcta.")
            self.puntuacion += 10
        else:
            print("⚠️ Era una trampa.")
            self.puntuacion -= 5

    def resolver_misterio(self):
        print("\n🔍 Elige la ruta del hacker (ej. A C D):")
        eleccion = input(">> ").upper().split()
        if eleccion == self.ruta_correcta:
            print("\n✅ ¡Atrápalo!")
            self.puntuacion += 50
            return True
        else:
            print("\n❌ Fallaste la ruta.")
            self.vidas -= 1
            return False

    def jugar(self):
        print("🎮 'Detective de Datos: El Misterio del Hacker Fantasma'")
        inicio = time.time()
        while True:
            if self.vidas <= 0 or time.time() - inicio > self.tiempo_total:
                print("\n⏳ Fin del juego. El hacker escapó.")
                break

            print(f"\n❤️ Vidas: {self.vidas} | 🏆 Puntuación: {self.puntuacion} | ⏰ Tiempo restante: {max(0, self.tiempo_total - int(time.time() - inicio))} s")
            self.mostrar_ruta()
            self.analizar_eventos()

            actual = self.servidores
            while actual:
                self.hackear_servidor(actual)
                actual = actual.siguiente

            if input("\n¿Reparar servidor hackeado? (s/n): ") == "s":
                nom = input("Servidor (A-E): ").upper()
                actual = self.servidores
                while actual:
                    if actual.nombre == nom and actual.hackeado:
                        self.reparar_servidor(actual)
                        break
                    actual = actual.siguiente

            self.investigar()

            if self.resolver_misterio():
                print("\n🎉 ¡Ganaste!")
            else:
                print("👻 El hacker escapó.")

            if input("\n¿Jugar otra vez? (s/n): ") != "s":
                print(f"Gracias por jugar. Puntuación final: {self.puntuacion}")
                break

if __name__ == "__main__":
    juego = DetectiveDigital()
    juego.jugar()
