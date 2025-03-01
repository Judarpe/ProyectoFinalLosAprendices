import pandas as pd
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px

#Crear barra lateral
def generarMenu():
    with st.sidebar:
        st.header("Redes Comunitarias")
        # st.header("Análisis de la Distribución de Atenciones de Salud en el municipio de Medellín.")
        col1,col2=st.columns(2)
        with col1:            
            imagen=Image.open("Media\Sisben.jpg")
            
            st.image(imagen,use_container_width=False,width=120)
        with col2:
            imagen=Image.open("Media\EscudoMedellin.png")
            st.image(imagen,use_container_width=False,width=95)
        
        st.page_link("app.py",label="Inicio",icon='🏠')
        st.page_link("Pages/informe.py",label="Informe",icon="📃")

def mostrartabla(df,titulo):
    df2=pd.DataFrame(df)
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    st.write(df2.head(100),unsafe_allow_html=False,)

def grafLineasMensual(df,Titulo,sisben,fecha,valor):
    st.markdown(f"<center><b>{Titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Asegurarse de que la columna de fechas sea de tipo datetime
    df[fecha] = pd.to_datetime(df[fecha])

    # Extraer el mes y el año de la columna de fechas
    df['Mes'] = df[fecha].dt.to_period('M')

    # Obtener los niveles únicos de Sisbén
    niveles_sisben = df[sisben].unique()

    # Crear el gráfico de líneas
    plt.figure(figsize=(10, 6))

    # Iterar sobre cada nivel de Sisbén y crear una línea
    for nivel in niveles_sisben:
        df_nivel = df[df[sisben] == nivel]
        datos_mensuales = df_nivel.groupby('Mes')[valor].count() / 1000  # Dividir por 1000
        plt.plot(datos_mensuales.index.astype(str), datos_mensuales.values, marker='o', label=f'Sisbén {nivel}')

    plt.xlabel("Mes")
    plt.ylabel(f"{valor} (Millares)")  # Actualizar la etiqueta del eje Y
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)
        
def grafBarras(df, titulo, X, Y):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Agrupar los datos por la columna X y calcular la media de la columna Y
    datos_agrupados = df.groupby(X)[Y].mean().reset_index()

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = sns.barplot(x=X, y=Y, data=datos_agrupados, palette='pastel')

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = round((barra.get_height()),None)
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{altura}', ha='center', va='bottom')
    
    plt.title(titulo)
    plt.xlabel(X)
    plt.ylabel(Y)
    plt.tight_layout()
    st.pyplot(plt)

def grafBarrasAtenciones(df, titulo, X, Y):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Agrupar los datos por la columna X y calcular la media de la columna Y
    datos_agrupados = df.groupby(X)[Y].count().reset_index()

    
        
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    barras=sns.barplot(x=X, y=Y, data=datos_agrupados,palette='pastel')

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{altura:.2f}', ha='center', va='bottom')

    plt.title(titulo)
    plt.xlabel(X)
    plt.ylabel(Y)
    plt.tight_layout()
    st.pyplot(plt)

def grafCircularAtenciones(df,titulo,valores):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)

    # Contar las atenciones por sexo
    conteo = df[valores].value_counts()

    # Calcular porcentajes
    porcentajes = conteo / conteo.sum() * 100

    # Crear la paleta de colores pastel
    colores_pastel = sns.color_palette("pastel", len(conteo))

    # Crear etiquetas con cantidad y porcentaje
    etiquetas = [f'{sexo} ({cantidad}, {porcentaje:.1f}%)' for sexo, cantidad, porcentaje in zip(conteo.index, conteo.values, porcentajes)]

    # Crear el gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(conteo, labels=etiquetas, autopct='', startangle=90,colors=colores_pastel)
    plt.title(titulo)
    plt.tight_layout()
    st.pyplot(plt)

def grafTop3CentrosAtencion(df,titulo,X):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Contar las atenciones por centro de atención
    conteo = df[X].value_counts().nlargest(3)

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = sns.barplot(x=conteo.index, y=conteo.values, palette="viridis")

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura)}', ha='center', va='bottom')

    plt.title(titulo)
    plt.xlabel("Centro de Atención")
    plt.ylabel("Número de Atenciones")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

def grafAtencionesSexo(df):
    st.markdown("Atenciones por Sexo")
    sns.set_style("whitegrid")

    # Contar las atenciones por sexo
    conteo_sexo = df['SEXO'].value_counts()

    # Crear el gráfico de barras
    plt.figure(figsize=(8, 6))
    barras = sns.barplot(x=conteo_sexo.index, y=conteo_sexo.values, palette="pastel")

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura)}', ha='center', va='bottom')

    plt.title("Atenciones por Sexo")
    plt.xlabel("Sexo")
    plt.ylabel("Número de Atenciones")
    plt.tight_layout()
    st.pyplot(plt)

def grafAtencionesRangoEdad(df,titulo,Edad):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Definir los rangos de edad y sus etiquetas
    rangos_edad = [0, 6, 12, 19, 27, 60, float('inf')]
    etiquetas_edad = ['Primera infancia 0 a 5', 'Infancia 6 a 11', 'Adolescencia 12 a 18', 'Juventud 19 a 27', 'Adultez 27 a 60', 'Vejez +60']

    # Crear una nueva columna 'RANGO_EDAD' con los rangos de edad
    df['RANGO_EDAD'] = pd.cut(df[Edad], bins=rangos_edad, labels=etiquetas_edad, right=False)

    # Contar las atenciones por rango de edad
    conteo_rangos = df['RANGO_EDAD'].value_counts().sort_index()

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = sns.barplot(x=conteo_rangos.index, y=conteo_rangos.values, palette="viridis")

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura)}', ha='center', va='bottom')

    plt.title(titulo)
    plt.xlabel("Rango de Edad")
    plt.ylabel("Número de Atenciones")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

def grafTop5Barrios(df,titulo,X):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Contar las atenciones por barrio
    conteo_barrios = df[X].value_counts().nlargest(5)

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = sns.barplot(x=conteo_barrios.index, y=conteo_barrios.values, palette="viridis")

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura)}', ha='center', va='bottom')

    plt.title(titulo)
    plt.xlabel("Barrio")
    plt.ylabel("Número de Atenciones")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

def grafMapaCentrosAtencion(df,titulo,Marcadores,longitud,latitud):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)

    # Agrupar los datos por centro de atención y calcular la cantidad de atenciones y barrios atendidos
    centros_agrupados = df.groupby([Marcadores,longitud,latitud]).agg(
        Atenciones=(Marcadores, 'count'),
        Barrios=('BARRIO', lambda x: ', '.join(set(x)))
    ).reset_index()

    # Crear el mapa interactivo
    fig = px.scatter_mapbox(
        centros_agrupados,
        lat=latitud,
        lon=longitud,
        size="Atenciones",
        size_max=40,  # Ajusta el tamaño máximo de los indicadores
        color="Atenciones",
        color_continuous_scale="viridis",
        hover_name=Marcadores,
        hover_data={"Atenciones": True, "Barrios": True, "LATITUD": False, "LONGITUD": False},
        zoom=10,  # Ajusta el nivel de zoom inicial
        mapbox_style="carto-positron"
    )

    fig.update_layout(mapbox_style="carto-positron")

    st.plotly_chart(fig)

def grafTop3CentrosAtencionSisben(df, X, Y, nivel_deseado):
    sns.set_style("whitegrid")

    # Filtrar el DataFrame para el nivel deseado
    df_nivel = df[df[Y] == nivel_deseado]

    if df_nivel.empty:
        st.warning(f"No hay datos para el nivel de Sisbén: {nivel_deseado}")
        return

    # Contar las atenciones por centro de atención
    conteo_centros = df_nivel[X].value_counts().nlargest(3)

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = sns.barplot(x=conteo_centros.index, y=conteo_centros.values, palette="viridis")

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura)}', ha='center', va='bottom')

    plt.title(f"Top 3 Centros de Atención - Nivel Sisbén {nivel_deseado}")
    plt.xlabel("Centro de Atención")
    plt.ylabel("Número de Atenciones")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

def grafTop5BarriosSisben(df, X, Y, nivel_deseado):
    sns.set_style("whitegrid")

    # Graficar solo el nivel deseado
    df_nivel = df[df[Y] == nivel_deseado]
    conteo_barrios = df_nivel[X].value_counts().nlargest(5)

    plt.figure(figsize=(10, 6))
    barras = sns.barplot(x=conteo_barrios.index, y=conteo_barrios.values, palette="viridis")

    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                    f'{int(altura)}', ha='center', va='bottom')

    plt.title(f"Top 5 Barrios - Nivel Sisbén {nivel_deseado}")
    plt.xlabel("Barrio")
    plt.ylabel("Número de Atenciones")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

def grafAfiliadosSexoAgrupado(df,titulo,X,Y):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Crear el gráfico de barras agrupadas
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x=X, hue=Y, data=df)

    # Añadir etiquetas de texto con los valores en cada barra
    for p in ax.patches:
        altura = p.get_height()
        ax.annotate(f'{int(altura)}', (p.get_x() + p.get_width() / 2., altura),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    plt.title(titulo)
    plt.xlabel("Sexo")
    plt.ylabel("Cantidad")
    plt.legend(title="Tipo de Afiliado")
    plt.tight_layout()
    st.pyplot(plt)

def grafEdadPromedioAfiliadoApiladoColores(df,titulo,X,Y):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)

    # Agrupar los datos por tipo de afiliado y calcular la edad promedio
    edad_promedio_afiliado = df.groupby(X)[Y].mean().reset_index()

    # Crear una lista de colores personalizada
    colores = ['skyblue', 'salmon', 'lightgreen']  # Puedes elegir los colores que prefieras

    # Crear el gráfico de barras con colores personalizados
    plt.figure(figsize=(10, 6))
    barras = plt.bar(edad_promedio_afiliado[X], edad_promedio_afiliado[Y], color=colores)

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras:
        altura = round(barra.get_height(),None)
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{altura}', ha='center', va='bottom')

    plt.title(titulo)
    plt.xlabel("Tipo de Afiliado")
    plt.ylabel("Edad Promedio")
    plt.xticks(rotation=0)
    plt.tight_layout()
    st.pyplot(plt)

def grafServiciosAfiliado(df,titulo,X):
    st.markdown(f"<center><b>{titulo}</b></center>", unsafe_allow_html=True)
    sns.set_style("whitegrid")

    # Contar la cantidad de servicios por tipo de afiliado
    conteo_afiliados = df[X].value_counts()

    # Crear una lista de colores personalizada
    colores = sns.color_palette('pastel', len(conteo_afiliados))

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = sns.barplot(x=conteo_afiliados.index, y=conteo_afiliados.values, palette=colores)

    # Añadir etiquetas de texto con los valores en cada barra
    for barra in barras.patches:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura)}', ha='center', va='bottom')

    plt.title(titulo)
    plt.xlabel("Tipo de Afiliado")
    plt.ylabel("Cantidad de Servicios")
    plt.xticks(rotation=0)
    plt.tight_layout()
    st.pyplot(plt)