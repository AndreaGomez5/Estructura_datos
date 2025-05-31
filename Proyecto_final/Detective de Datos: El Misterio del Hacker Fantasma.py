import random, time, hashlib
from sklearn.tree import DecisionTreeClassifier

class NodoServidor:
    def __init__(self, nombre): self.nombre, self.siguiente, self.hackeado = nombre, None, False

class ColaEventos:
    def __init__(self): self.eventos = []
    def encolar(self, e): self.eventos.append(e)
    def desencolar(self): return self.eventos.pop(0) if self.eventos else None
    def esta_vacia(self): return not self.eventos

class ArbolEvidencia:
    def __init__(self, dato, izq=None, der=None): self.dato, self.izquierda, self.derecha = dato, izq, der
    def imprimir(self, nivel=0):
        if self.derecha: self.derecha.imprimir(nivel+1)
        print("    " * nivel + f"🔍 {self.dato}")
        if self.izquierda: self.izquierda.imprimir(nivel+1)

class DetectiveDigital:
    def __init__(self):
        self.servidores = self.crear_red()
        self.eventos = ColaEventos()
        self.ruta_correcta = random.sample("ABCDE", 3)
        self.evidencia = self.generar_arbol_evidencia()
        self.vidas, self.puntuacion, self.tiempo_total = 3, 0, 120
        self.modelo_ml = self.entrenar_modelo()

    def crear_red(self):
        nombres = [NodoServidor(n) for n in "ABCDE"]
        for a, b in zip(nombres, nombres[1:]): a.siguiente = b
        return nombres[0]

    def generar_arbol_evidencia(self):
        return ArbolEvidencia("IP sospechosa",
            ArbolEvidencia("Correo filtrado"),
            ArbolEvidencia("Acceso remoto", ArbolEvidencia("VPN privada"), ArbolEvidencia("Archivo cifrado"))
        )

    def entrenar_modelo(self):
        X, y = [], []
        for _ in range(1000):
            h, n, c = random.randint(0,23), random.randint(0,4), random.randint(0,100)
            X.append([n,h,c]); y.append(1 if c > 70 or h >= 22 or h <= 3 else 0)
        modelo = DecisionTreeClassifier()
        modelo.fit(X,y)
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
        for _ in range(3):
            t = random.randint(1,2)
            time.sleep(t)
            e = random.choice(["Ping inusual", "Conexión segura detectada", "Paquete dañado", 
                               "Error 404", "Conexión fallida", "Posible hacker"])
            self.eventos.encolar(e)
            print(f" + Evento: {e} ({t}s)")

    def predecir_hackeo(self, nombre):
        return self.modelo_ml.predict([[ord(nombre)-65, time.localtime().tm_hour, random.randint(0,100)]])[0] == 1

    def hackear_servidor(self, s):
        if self.predecir_hackeo(s.nombre):
            s.hackeado = True
            print(f"⚠️ {s.nombre} hackeado")
        else:
            print(f"💻 {s.nombre} seguro")

    def reparar_servidor(self, s):
        print(f"\n🔧 Reparando {s.nombre}...")
        time.sleep(random.randint(5,10))
        if random.choice([1,0]):
            s.hackeado = False
            print("✅ Éxito."); self.puntuacion += 15
        else:
            print("❌ Fallo."); self.puntuacion -= 10

    def generar_contraseña(self):
        return hashlib.sha256(str(random.randint(1000,9999)).encode()).hexdigest()[:6]

    def resolver_contraseña(self):
        print("\n🧩 Resuelve la contraseña")
        r = self.generar_contraseña()
        for i in range(3,0,-1):
            if input(f"Contraseña ({i} intentos): ") == r:
                print("✅ Correcta"); self.puntuacion += 20; return True
            print("❌ Incorrecta")
        print(f"❌ Era: {r}"); self.puntuacion -= 15; return False

    def investigar(self):
        print("\n🕵️ Revisando evidencia:")
        self.evidencia.imprimir()
        if input("\n¿Seguir izquierda o derecha? (i/d): ").lower() == "d":
            print("📁 Correcta"); self.puntuacion += 10
        else:
            print("⚠️ Trampa"); self.puntuacion -= 5

    def resolver_misterio(self):
        print("\n🔍 Ruta del hacker (ej. A C D):")
        if input(">> ").upper().split() == self.ruta_correcta:
            print("✅ ¡Atrápalo!"); self.puntuacion += 50; return True
        print("❌ Fallaste"); self.vidas -= 1; return False

    def jugar(self):
        print("🎮 Detective de Datos: Misterio del Hacker Fantasma")
        inicio = time.time()
        while self.vidas > 0 and time.time() - inicio < self.tiempo_total:
            print(f"\n❤️ {self.vidas} | 🏆 {self.puntuacion} | ⏰ {self.tiempo_total - int(time.time() - inicio)} s")
            self.mostrar_ruta()
            self.analizar_eventos()

            actual = self.servidores
            while actual: self.hackear_servidor(actual); actual = actual.siguiente

            if input("\n¿Reparar? (s/n): ") == "s":
                nom = input("Servidor (A-E): ").upper()
                actual = self.servidores
                while actual:
                    if actual.nombre == nom and actual.hackeado:
                        self.reparar_servidor(actual)
                        break
                    actual = actual.siguiente

            self.investigar()
            if self.resolver_misterio():
                print("🎉 ¡Ganaste!")
            else:
                print("👻 Escapó el hacker")

            if input("\n¿Otra vez? (s/n): ") != "s":
                break
        print(f"Gracias por jugar. Puntuación final: {self.puntuacion}")

if __name__ == "__main__":
    DetectiveDigital().jugar() 