import streamlit as st


def mostrar_grabacion():
     st.title("🎙️ Grabación de Audio desde el Navegador")
     audio_grabado = st.audio_input("Presiona para grabar tu voz",key="uploader_grabacion")
     if audio_grabado:
        st.success("✅ Grabación realizada")
        st.audio(audio_grabado, format="audio/wav")
        if st.button("Continuar"):
           from procesamiento import procesar_audio

           procesar_audio(audio_grabado)
    # Guardar el audio como archivo
        with open("grabacion_desde_navegador.wav", "wb") as f:
          f.write(audio_grabado.getbuffer())
        st.info("Archivo guardado como 'grabacion_desde_navegador.wav'")

