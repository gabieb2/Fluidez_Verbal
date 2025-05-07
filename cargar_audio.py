import streamlit as st
import audiofile as af
import tempfile

def mostrar_carga():
    audio_grabado = st.file_uploader("Sube un audio", type=["wav", "mp3"], key="uploader_carga")

    if audio_grabado:
        st.audio(audio_grabado)

        if st.button("Continuar", key="continuar_cargar"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_grabado.read())
                tmp_path = tmp.name

            # Leer el archivo con audiofile
            data, samplerate = af.read(tmp_path)

            # Guardar como WAV, si querés
            af.write("salida.wav", data, samplerate)

            # Procesar
            from procesamiento import procesar_audio
            procesar_audio(tmp_path)
