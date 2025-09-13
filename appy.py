import streamlit as st
import math

st.title("📐 Calculadora de Volumen de Figuras 3D")

# Lista de figuras
figuras = {
    "Cubo": ["Arista"],
    "Esfera": ["Radio"],
    "Cilindro": ["Radio", "Altura"],
    "Cono": ["Radio", "Altura"],
    "Prisma rectangular": ["Largo", "Ancho", "Altura"],
    "Pirámide": ["Área de la base", "Altura"]
}

# Selección de figura
figura = st.selectbox("Selecciona la figura tridimensional:", list(figuras.keys()))

# Botón para ingresar datos
if st.button("Ingresar dimensiones"):
    st.session_state.ingresar = True
else:
    if "ingresar" not in st.session_state:
        st.session_state.ingresar = False

# Mostrar inputs solo si se presionó el botón "Ingresar dimensiones"
if st.session_state.ingresar:
    dimensiones = {}
    for dim in figuras[figura]:
        dimensiones[dim] = st.number_input(f"Ingrese {dim}:", min_value=0.0, format="%.4f")

    # Botón para calcular volumen
    if st.button("Calcular volumen"):
        volumen = None

        if figura == "Cubo":
            a = dimensiones["Arista"]
            volumen = a ** 3
        elif figura == "Esfera":
            r = dimensiones["Radio"]
            volumen = (4/3) * math.pi * (r ** 3)
        elif figura == "Cilindro":
            r = dimensiones["Radio"]
            h = dimensiones["Altura"]
            volumen = math.pi * (r ** 2) * h
        elif figura == "Cono":
            r = dimensiones["Radio"]
            h = dimensiones["Altura"]
            volumen = (1/3) * math.pi * (r ** 2) * h
        elif figura == "Prisma rectangular":
            l = dimensiones["Largo"]
            w = dimensiones["Ancho"]
            h = dimensiones["Altura"]
            volumen = l * w * h
        elif figura == "Pirámide":
            base = dimensiones["Área de la base"]
            h = dimensiones["Altura"]
            volumen = (1/3) * base * h
