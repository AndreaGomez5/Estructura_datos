import random, time, hashlib
from sklearn.tree import DecisionTreeClassifier

class NodoServidor:
    def __init__(s, n): s.nombre, s.siguiente, s.hackeado = n, None, False

class ColaEventos:
    def __init__(s): s.e = []
    def encolar(s, x): s.e.append(x)
    def desencolar(s): return s.e.pop(0) if s.e else None
    def esta_vacia(s): return not s.e

class ArbolEvidencia:
    def __init__(s, d, i=None, d_=None): s.dato, s.izquierda, s.derecha = d, i, d_
    def imprimir(s, n=0):
        if s.derecha: s.derecha.imprimir(n+1)
        print("    "*n + f"🔍 {s.dato}")
        if s.izquierda: s.izquierda.imprimir(n+1)

class DetectiveDigital:
    def __init__(s):
        s.servidores = s.crear_red()
        s.eventos, s.ruta_correcta = ColaEventos(), random.sample("ABCDE", 3)
        s.evidencia = s.gen_arbol()
        s.vidas, s.punt, s.tiempo_total = 3, 0, 120
        s.modelo = s.entrenar()

    def crear_red(s):
        nodos = [NodoServidor(c) for c in "ABCDE"]
        for a, b in zip(nodos, nodos[1:]): a.siguiente = b
        return nodos[0]

    def gen_arbol(s):
        return ArbolEvidencia("IP sospechosa", ArbolEvidencia("Correo filtrado"),
            ArbolEvidencia("Acceso remoto", ArbolEvidencia("VPN privada"), ArbolEvidencia("Archivo cifrado")))

    def entrenar(s):
        X = [[random.randint(0,4), random.randint(0,23), random.randint(0,100)] for _ in range(1000)]
        y = [1 if c[2]>70 or c[1]>=22 or c[1]<=3 else 0 for c in X]
        m = DecisionTreeClassifier(); m.fit(X,y); return m

    def mostrar_ruta(s):
        print("\n🌐 Red de servidores:")
        a = s.servidores
        while a:
            print(f" -> Servidor {a.nombre} (Hackeado: {'Sí' if a.hackeado else 'No'})", end="")
            a = a.siguiente
        print()

    def analizar_eventos(s):
        print("\n📡 Analizando eventos de red...")
        for _ in range(3):
            t = random.randint(1,2); time.sleep(t)
            e = random.choice(["Ping inusual", "Conexión segura detectada", "Paquete dañado",
                               "Error 404", "Conexión fallida", "Posible hacker"])
            s.eventos.encolar(e); print(f" + Evento: {e} ({t}s)")

    def predecir(s, nom):
        return s.modelo.predict([[ord(nom)-65, time.localtime().tm_hour, random.randint(0,100)]])[0] == 1

    def hackear(s, n):
        if s.predecir(n.nombre): n.hackeado = True; print(f"⚠️ {n.nombre} hackeado")
        else: print(f"💻 {n.nombre} seguro")

    def reparar(s, n):
        print(f"\n🔧 Reparando {n.nombre}..."); time.sleep(random.randint(5,10))
        if random.choice([1,0]): n.hackeado = False; print("✅ Éxito."); s.punt += 15
        else: print("❌ Fallo."); s.punt -= 10

    def gen_pass(s): return hashlib.sha256(str(random.randint(1000,9999)).encode()).hexdigest()[:6]

    def resolver_pass(s):
        print("\n🧩 Resuelve la contraseña"); r = s.gen_pass()
        for i in range(3,0,-1):
            if input(f"Contraseña ({i} intentos): ") == r:
                print("✅ Correcta"); s.punt += 20; return True
            print("❌ Incorrecta")
        print(f"❌ Era: {r}"); s.punt -= 15; return False

    def investigar(s):
        print("\n🕵️ Revisando evidencia:"); s.evidencia.imprimir()
        if input("\n¿Seguir izquierda o derecha? (i/d): ").lower() == "d":
            print("📁 Correcta"); s.punt += 10
        else: print("⚠️ Trampa"); s.punt -= 5

    def resolver_misterio(s):
        print("\n🔍 Ruta del hacker (ej. A C D):")
        if input(">> ").upper().split() == s.ruta_correcta:
            print("✅ ¡Atrápalo!"); s.punt += 50; return True
        print("❌ Fallaste"); s.vidas -= 1; return False

    def jugar(s):
        print("🎮 Detective de Datos: Misterio del Hacker Fantasma")
        ini = time.time()
        while s.vidas > 0 and time.time()-ini < s.tiempo_total:
            print(f"\n❤️ {s.vidas} | 🏆 {s.punt} | ⏰ {s.tiempo_total - int(time.time()-ini)} s")
            s.mostrar_ruta(); s.analizar_eventos()
            a = s.servidores
            while a: s.hackear(a); a = a.siguiente
            if input("\n¿Reparar? (s/n): ") == "s":
                nom = input("Servidor (A-E): ").upper(); a = s.servidores
                while a:
                    if a.nombre == nom and a.hackeado: s.reparar(a); break
                    a = a.siguiente
            s.investigar()
            print("🎉 ¡Ganaste!" if s.resolver_misterio() else "👻 Escapó el hacker")
            if input("\n¿Otra vez? (s/n): ") != "s": break
        print(f"Gracias por jugar. Puntuación final: {s.punt}")

if __name__ == "__main__": DetectiveDigital().jugar()