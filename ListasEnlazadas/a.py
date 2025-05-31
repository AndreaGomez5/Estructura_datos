import streamlit as st
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
    def imprimir(s, nivel=0):
        res = ""
        if s.derecha: res += s.derecha.imprimir(nivel+1)
        res += "    "*nivel + f"🔍 {s.dato}\n"
        if s.izquierda: res += s.izquierda.imprimir(nivel+1)
        return res

@st.cache_resource
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

    def predecir(s, nom):
        return s.modelo.predict([[ord(nom)-65, time.localtime().tm_hour, random.randint(0,100)]])[0] == 1

    def gen_pass(s):
        return hashlib.sha256(str(random.randint(1000,9999)).encode()).hexdigest()[:6]

dd = DetectiveDigital()

# Estado del juego
if 'vidas' not in st.session_state:
    st.session_state.vidas = 3
    st.session_state.punt = 0
    st.session_state.servidores = dd.crear_red()
    st.session_state.contraseña = dd.gen_pass()
    st.session_state.ruta_correcta = dd.ruta_correcta
    st.session_state.revelada = False
    st.session_state.evidencia = dd.evidencia

st.title("🎮 Detective de Datos: Misterio del Hacker Fantasma")
st.write(f"❤️ Vidas: {st.session_state.vidas} | 🏆 Puntos: {st.session_state.punt}")

st.subheader("🌐 Red de Servidores")
actual = st.session_state.servidores
while actual:
    st.write(f"🔹 Servidor {actual.nombre} - Hackeado: {'✅' if actual.hackeado else '❌'}")
    actual = actual.siguiente

if st.button("📡 Analizar eventos"):
    eventos = ["Ping inusual", "Conexión segura detectada", "Paquete dañado",
               "Error 404", "Conexión fallida", "Posible hacker"]
    for _ in range(3):
        e = random.choice(eventos)
        st.session_state.punt += 1
        st.write(f"+ Evento: {e}")

if st.button("⚠️ Predecir hackeos"):
    actual = st.session_state.servidores
    while actual:
        if dd.predecir(actual.nombre):
            actual.hackeado = True
            st.write(f"🚨 {actual.nombre} fue hackeado!")
        else:
            st.write(f"🛡️ {actual.nombre} está seguro.")
        actual = actual.siguiente

st.subheader("🔧 Reparar servidor")
servidor = st.selectbox("Elige un servidor", [c for c in "ABCDE"])
if st.button("Reparar"):
    actual = st.session_state.servidores
    while actual:
        if actual.nombre == servidor and actual.hackeado:
            if random.choice([1,0]):
                actual.hackeado = False
                st.session_state.punt += 15
                st.success(f"{servidor} reparado correctamente.")
            else:
                st.session_state.punt -= 10
                st.error(f"Falló la reparación de {servidor}.")
            break
        actual = actual.siguiente

st.subheader("🧩 Contraseña")
pass_input = st.text_input("Ingresa la contraseña de 6 caracteres")
if st.button("Verificar contraseña"):
    if pass_input == st.session_state.contraseña:
        st.session_state.punt += 20
        st.success("Contraseña correcta!")
        st.session_state.contraseña = dd.gen_pass()
    else:
        st.session_state.punt -= 5
        st.error("Incorrecta")

st.subheader("🕵️ Evidencia")
if st.button("Ver evidencia"):
    st.text(dd.evidencia.imprimir())
    if st.radio("¿Izquierda o derecha?", ["Izquierda", "Derecha"]) == "Derecha":
        st.session_state.punt += 10
        st.success("¡Correcto!")
    else:
        st.session_state.punt -= 5
        st.warning("¡Era una trampa!")

st.subheader("🔍 Resolver el misterio")
ruta = st.text_input("Ruta del hacker (ej. A C D)")
if st.button("Resolver"):
    if ruta.upper().split() == st.session_state.ruta_correcta:
        st.session_state.punt += 50
        st.balloons()
        st.success("¡Atrápalo! Has resuelto el misterio")
        st.session_state.revelada = True
    else:
        st.session_state.vidas -= 1
        st.warning("Fallaste. El hacker escapó.")

if st.session_state.vidas <= 0:
    st.error("Juego terminado. Vuelve a intentarlo.")
    if st.button("Reiniciar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
