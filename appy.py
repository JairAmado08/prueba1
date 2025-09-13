import streamlit as st
import math

st.title("📐 Calculadora de Volumen de Figuras 3D")

# Diccionario con las figuras, dimensiones y URLs de imagen representativa
figuras = {
    "Cubo": {
        "dimensiones": ["Arista"],
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Cube_simple.svg/200px-Cube_simple.svg.png"
    },
    "Esfera": {
        "dimensiones": ["Radio"],
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Sphere_wireframe_10deg_6r.svg/200px-Sphere_wireframe_10deg_6r.svg.png"
    },
    "Cilindro": {
        "dimensiones": ["Radio", "Altura"],
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Cylinder_geometry.svg/200px-Cylinder_geometry.svg.png"
    },
    "Cono": {
        "dimensiones": ["Radio", "Altura"],
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Cone_geometry.svg/200px-Cone_geometry.svg.png"
    },
    "Prisma rectangular": {
        "dimensiones": ["Largo", "Ancho", "Altura"],
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Rectangular_prism.svg/200px-Rectangular_prism.svg.png"
    },
    "Pirámide": {
        "dimensiones": ["Área de la base", "Altura"],
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Square_pyramid.svg/200px-Square_pyramid.svg.png"
    }
}

# Selección de figura
figura = st.selectbox("Selecciona la figura tridimensional:", list(figuras.keys()))

# Mostrar imagen de la figura
st.image(figuras[figura]["imagen"], width=200)

st.markdown("### Ingresa las dimensiones:")

# Inputs de dimensiones
dimensiones = {}
for dim in figuras[figura]["dimensiones"]:
    dimensiones[dim] = st.number_input(f"{dim}:", min_value=0.0, format="%.4f")

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

    if volumen is not None:
        st.success(f"El volumen del {figura.lower()} es: **{volumen:.4f} unidades cúbicas**")
