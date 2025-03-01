import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns
import utilidades as util
import numpy as np
from PIL import Image

# Graficos para el Proyecto
# 1- Cantidad de Atenciones Según Nivel del Sisben - OK
# 2- Edad Poblacional [ 3 Graficos ] - 
# 3- TOP 3 Global de Centros de Atención
# 4- TOP 3 de Centros de Atención, con más atenciones segun el nivel del sisben.
# 5- Atenciones x Sexo
# 6- Edades de Atención [ Mirar rangos de edad para atenciòn medica ]
# 7- TOP 5 de los barrios con más atención, y nivel de Sisben
# 9- Grafico de Latitud + Longitud

#Configuramos encabezados de pagina
st.set_page_config(
    page_title="Los Aprendices",
    page_icon=":ethoscope:",
    initial_sidebar_state="expanded",
    layout="centered"
)

@st.cache_data
def cargar_dataframe(ruta_archivo):
    """Carga el DataFrame desde un archivo CSV."""
    df = pd.read_csv(ruta_archivo,compression='bz2')
    return df
ruta_del_archivo = "Data\Perfil_demografico_Final.csv"  # Reemplaza con la ruta de tu archivo
df = cargar_dataframe(ruta_del_archivo)

util.generarMenu()

#Visualización
st.markdown("<h1 style='text-align: center;'>Gráficos para informe</h1>", unsafe_allow_html=True)

util.mostrartabla(df,"PERFIL DEMOGRAFICO DE ATENCIONES DE SAVIA SALUD")

imagensisben=Image.open("Media/NivelSisben.jpg")
st.image(imagensisben,use_container_width=False,width=1000)

#Configuramos columnas
col1,col2,col3=st.columns([0.5,100,0.5],
                        vertical_alignment="top"
                        )
with col2:
    # 1- Cantidad de Atenciones Según Nivel del Sisben
    util.grafLineasMensual(df,"Gráfico de líneas por nivel de Sisbén (valores en millares)","NIVEL_SISBEN",'FECHA','NIVEL_SISBEN')

    colin1,colin2=st.columns([1,1],
                        vertical_alignment="top"
                        )
    # 2- Edad Poblacional [ 3 Graficos ]
    with colin1:
        util.grafBarras(df,"EDAD PROMEDIO SEGUN SEXO","SEXO","EDAD")
    with colin2:
        util.grafCircularAtenciones(df,"ATENCIONES POR SEXO","SEXO")

       
    util.grafBarras(df,"EDAD PROMEDIO SEGUN NIVEL DE SISBEN","NIVEL_SISBEN","EDAD")
    
# 3- TOP 3 Global de Centros de Atención

    util.grafTop3CentrosAtencion(df,"Top 3 Centros de Atención con Más Atenciones","CENTRO_ATENCION")

# 4- TOP 3 de Centros de Atención, con más atenciones segun el nivel del sisben.
    colin3,colin4=st.columns([1,1],
                        vertical_alignment="top"
                        )   
    
    with colin3:
        util.grafTop3CentrosAtencionSisben(df,'CENTRO_ATENCION','NIVEL_SISBEN','A')
        util.grafTop3CentrosAtencionSisben(df,'CENTRO_ATENCION','NIVEL_SISBEN','C')
    with colin4:
        util.grafTop3CentrosAtencionSisben(df,'CENTRO_ATENCION','NIVEL_SISBEN','B')
        util.grafTop3CentrosAtencionSisben(df,'CENTRO_ATENCION','NIVEL_SISBEN','D')    

# 5- Atenciones x Sexo
    util.grafAtencionesSexo(df)

# 6- Edades de Atención [ Mirar rangos de edad para atenciòn medica ]

    util.grafAtencionesRangoEdad(df,"Cantidad de Atenciones por Rango de Edad",'EDAD')

# 7- TOP 5 de los barrios con más atención, y nivel de Sisben

    util.grafTop5Barrios(df,"Top 5 Barrios con Más Atenciones",'BARRIO')
    colin5,colin6=st.columns([1,1],
                        vertical_alignment="top"
                        )   
    with colin5:
        util.grafTop5BarriosSisben(df,'BARRIO','NIVEL_SISBEN','A')
        util.grafTop5BarriosSisben(df,'BARRIO','NIVEL_SISBEN','C')
    with colin6:
        util.grafTop5BarriosSisben(df,'BARRIO','NIVEL_SISBEN','B')
        util.grafTop5BarriosSisben(df,'BARRIO','NIVEL_SISBEN','D')

# 9- Grafico de Latitud + Longitud

util.grafMapaCentrosAtencion(df,"Mapa de Centros de Atención",'CENTRO_ATENCION','LONGITUD', 'LATITUD')

util.grafAfiliadosSexoAgrupado(df,'Tipos de Afiliado por Sexo','SEXO','TIPO_AFILIADO')
util.grafAfiliadosSexoAgrupado(df,'Nivel de SISBEN por Sexo','SEXO','NIVEL_SISBEN')

util.grafEdadPromedioAfiliadoApiladoColores(df,'Edad Promedio por Tipo de Afiliado','TIPO_AFILIADO','EDAD')

util.grafServiciosAfiliado(df,"Cantidad de Servicios por Tipo de Afiliado",'TIPO_AFILIADO',)