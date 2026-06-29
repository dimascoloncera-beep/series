import streamlit as st

st.title("Gráfica de serie de tiempo")

entrada = st.text_input(
    "Ingrese la serie, separada por comas:",
    value="10,15,18,26,31"
)

# Divide el texto y elimina espacios
entrada2 = [x.strip() for x in entrada.split(",")]

# Convierte a números
serie = [float(i) for i in entrada2]

# Muestra la lista
st.write("Serie:", serie)

# Grafica
st.line_chart(serie)
