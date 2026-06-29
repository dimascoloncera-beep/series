import streamlit as st
st.title("Grafica de series de tiempo")

serie = [10, 15, 18, 26, 31]
st.line_chart(serie)