import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir grafico dispersion') # crear un botón

st.title("Python Plotting Program")
st.subheader("Este es un programa en Python que genera un histograma y un gráfico de dispersión utilizando un dataset de muestra. El programa carga un archivo CSV, selecciona las columnas especificadas y visualiza los gráficos.")

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price") 

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
