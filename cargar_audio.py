import streamlit as st



def mostrar_carga():
    audio_grabado = st.file_uploader("Sube un audio", type=["wav", "mp3"],key="uploader_carga")
    if audio_grabado:
        st.audio(audio_grabado)
        st.session_state["audio"] = audio_grabado.read()
        if st.button("Continuar"):
           from procesamiento import procesar_audio
           procesar_audio(audio_grabado)
