import pandas as pd
import utilidades as util
import streamlit as st
from PIL import Image

#para correr streamlit se ejecuta: streamlit run app.py

#Pagina d epresentación o Index
st.set_page_config(
    page_title="Los Aprendices",
    initial_sidebar_state="auto",
    layout="wide",
    page_icon=":hospital:"
)

# adicionar pagina con leeeme o info, con documentación del proyecto, libk bd y como se realizó la limpieza.

#llamamos la funcion utilidades
util.generarMenu()

# Estructura de presentación
left_col, center_col, right_col = st.columns([1, 4, 1], vertical_alignment="center")

# Edito la columna central para el título
with center_col:
    st.markdown("<h3 style='text-align: center;'>Análisis de la Distribución de Atenciones de Salud, en el Municipio de Medellín.</h3>", unsafe_allow_html=True)

# Edito la columna central para el título
with center_col:
    st.markdown("<h4 style='text-align: center;'>Objetivo</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>Analizar la distribución de las atenciones de salud en el Municipio de Medellín; tomando como base la categorización del Sisben, genero y edad.</h6>", unsafe_allow_html=True)

# Edito la columna central para el título
with center_col:
    st.markdown("<h1 style='text-align: center;'>Equipo Los Aprendices</h1>", unsafe_allow_html=True)

# Crear la cuadrícula de 4 columnas dentro de la columna central
with center_col:
    col1, col2, col3, col4 = st.columns(4)  # Cuatro columnas

    # Primera fila (todas las columnas)
    with col1:
        imagen1 = Image.open("Media/Tombe.jpg")  # Reemplaza con la ruta correcta
        st.image(imagen1, use_container_width=False, width=150, caption="Yenny Tombe")

    with col2:
        imagen2 = Image.open("Media/Navarro.jpg")  # Reemplaza con la ruta correcta
        st.image(imagen2, use_container_width=False, width=150, caption="Yesica Navarro")

    with col3:
        imagen3 = Image.open("Media/Areiza.jpg")  # Reemplaza con la ruta correcta
        st.image(imagen3, use_container_width=False, width=150, caption="Juan Areiza")

    with col4:
        imagen4 = Image.open("Media/Zapata.jpg")  # Reemplaza con la ruta correcta
        st.image(imagen4, use_container_width=False, width=150, caption="Diego Zapata")
        
        