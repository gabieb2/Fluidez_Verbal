import streamlit as st
import audiofile as af
import tempfile

def mostrar_carga():
    audio_grabado = st.file_uploader("Sube un audio", type=["wav", "mp3"], key="uploader_carga")
    
    if audio_grabado:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3" if audio_grabado.type == "audio/mp3" else ".wav") as tmp:
            tmp.write(audio_grabado.read())
            audio_path = tmp.name
        
        st.audio(audio_path)
        
        if st.button("Continuar", key="continuar_cargar"):
            # Leer el archivo usando audiofile
            data, samplerate = af.read(audio_path)

            # Guardar el archivo como WAV si es necesario
            output_path = audio_path.replace(".mp3", ".wav") if audio_grabado.type == "audio/mp3" else audio_path
            af.write(output_path, data, samplerate)

            # Abrir el archivo antes de pasárselo a procesar_audio
            with open(output_path, "rb") as file:
                from procesamiento import procesar_audio
                procesar_audio(file)  # Ahora se pasa el archivo abierto, no la ruta
