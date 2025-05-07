import streamlit as st
from cargar_audio import mostrar_carga
from grabar_audio import mostrar_grabacion

import subprocess

try:
    subprocess.run(["ffmpeg", "-version"], check=True)
    print("ffmpeg está instalado correctamente")
except FileNotFoundError:
    print("ffmpeg no está instalado")
    st.error("❌ ffmpeg no está instalado. Por favor, instálalo para usar esta aplicación.")
    
st.title("Detector de fluidez verbal")
st.write("Esta aplicación permite cargar o grabar un audio y analizar su fluidez verbal.")

tab_cargar, tab_grabar = st.tabs(["📂 Cargar audio", "🎙️ Grabar audio"])

with tab_cargar:
    mostrar_carga()

with tab_grabar:
    mostrar_grabacion()


