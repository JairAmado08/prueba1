import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # necesario para gráficos 3D

st.title("📐 Calculadora de Volumen de Figuras 3D con Gráficos 3D")

figuras = {
    "Cubo": {
        "dimensiones": ["Arista"],
    },
    "Esfera": {
        "dimensiones": ["Radio"],
    },
    "Cilindro": {
        "dimensiones": ["Radio", "Altura"],
    },
    "Cono": {
        "dimensiones": ["Radio", "Altura"],
    },
    "Prisma rectangular": {
        "dimensiones": ["Largo", "Ancho", "Altura"],
    },
    "Pirámide": {
        "dimensiones": ["Área de la base", "Altura"],  # para simplificar, la base será cuadrada aquí
    }
}

figura = st.selectbox("Selecciona la figura tridimensional:", list(figuras.keys()))

st.markdown("### Ingresa las dimensiones:")

dimensiones = {}
for dim in figuras[figura]["dimensiones"]:
    dimensiones[dim] = st.number_input(f"{dim}:", min_value=0.0, format="%.4f")

def plot_cubo(a):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    r = [0, a]
    for s, e in zip(
        [(r[0], r[0], r[0]), (r[0], r[0], r[1]), (r[0], r[1], r[0]), (r[0], r[1], r[1]),
         (r[1], r[0], r[0]), (r[1], r[0], r[1]), (r[1], r[1], r[0]), (r[1], r[1], r[1])],
        [(r[0], r[0], r[1]), (r[0], r[1], r[0]), (r[0], r[1], r[1]), (r[1], r[0], r[0]),
         (r[1], r[0], r[1]), (r[1], r[1], r[0]), (r[1], r[1], r[1]), (r[0], r[0], r[0])]):
        ax.plot([s[0], e[0]], [s[1], e[1]], [s[2], e[2]], color='b')
    ax.set_box_aspect([1,1,1])
    ax.set_xlim(0,a); ax.set_ylim(0,a); ax.set_zlim(0,a)
    ax.set_title("Cubo")
    return fig

def plot_esfera(r):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
    x = r * np.cos(u) * np.sin(v)
    y = r * np.sin(u) * np.sin(v)
    z = r * np.cos(v)
    ax.plot_surface(x, y, z, color='c', alpha=0.6)
    ax.set_box_aspect([1,1,1])
    ax.set_title("Esfera")
    return fig

def plot_cilindro(r, h):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = np.linspace(0, h, 30)
    theta = np.linspace(0, 2 * np.pi, 30)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x = r * np.cos(theta_grid)
    y = r * np.sin(theta_grid)
    ax.plot_surface(x, y, z_grid, color='orange', alpha=0.6)
    ax.set_box_aspect([1,1,h/r])
    ax.set_title("Cilindro")
    return fig

def plot_cono(r, h):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2*np.pi, 30)
    z = np.linspace(0, h, 30)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x = (r * (h - z_grid) / h) * np.cos(theta_grid)
    y = (r * (h - z_grid) / h) * np.sin(theta_grid)
    ax.plot_surface(x, y, z_grid, color='green', alpha=0.6)
    ax.set_box_aspect([1,1,h/r])
    ax.set_title("Cono")
    return fig

def plot_prisma(l, w, h):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Vértices del prisma rectangular
    x = [0, l, l, 0, 0, l, l, 0]
    y = [0, 0, w, w, 0, 0, w, w]
    z = [0, 0, 0, 0, h, h, h, h]
    # Aristas a conectar
    edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
    for e in edges:
        ax.plot([x[e[0]], x[e[1]]], [y[e[0]], y[e[1]]], [z[e[0]], z[e[1]]], color='purple')
    ax.set_box_aspect([l,w,h])
    ax.set_title("Prisma Rectangular")
    return fig

def plot_piramide(base_area, h):
    # Para simplicidad, asumimos base cuadrada
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    base_side = math.sqrt(base_area)
    # Base cuadrada
    x = np.array([0, base_side, base_side, 0])
    y = np.array([0, 0, base_side, base_side])
    z = np.zeros(4)
    apex = np.array([base_side/2, base_side/2, h])

    # Dibujar base
    verts = [list(zip(x, y, z))]
    ax.plot_trisurf(x, y, z, color='red', alpha=0.3)

    # Dibujar aristas
    for i in range(4):
        ax.plot([x[i], apex[0]], [y[i], apex[1]], [z[i], apex[2]], color='red')
    # Base edges
    for i in range(4):
        ax.plot([x[i], x[(i+1)%4]], [y[i], y[(i+1)%4]], [z[i], z[(i+1)%4]], color='red')

    ax.set_box_aspect([base_side, base_side, h])
    ax.set_title("Pirámide")
    return fig

if st.button("Calcular volumen"):
    volumen = None
    fig_plot = None

    if figura == "Cubo":
        a = dimensiones["Arista"]
        volumen = a ** 3
        fig_plot = plot_cubo(a)
    elif figura == "Esfera":
        r = dimensiones["Radio"]
        volumen = (4/3) * math.pi * (r ** 3)
        fig_plot = plot_esfera(r)
    elif figura == "Cilindro":
        r = dimensiones["Radio"]
        h = dimensiones["Altura"]
        volumen = math.pi * (r ** 2) * h
        fig_plot = plot_cilindro(r, h)
    elif figura == "Cono":
        r = dimensiones["Radio"]
        h = dimensiones["Altura"]
        volumen = (1/3) * math.pi * (r ** 2) * h
        fig_plot = plot_cono(r, h)
    elif figura == "Prisma rectangular":
        l = dimensiones["Largo"]
        w = dimensiones["Ancho"]
        h = dimensiones["Altura"]
        volumen = l * w * h
        fig_plot = plot_prisma(l, w, h)
    elif figura == "Pirámide":
        base = dimensiones["Área de la base"]
        h = dimensiones["Altura"]
        volumen = (1/3) * base * h
        fig_plot = plot_piramide(base, h)

    if volumen is not None:
        st.success(f"El volumen del {figura.lower()} es: **{volumen:.4f} unidades cúbicas**")
        st.pyplot(fig_plot)
