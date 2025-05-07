import streamlit as st
import tempfile
import subprocess
import librosa
import whisper
import audiofile as af

def procesar_audio(audio):
    if audio is None:
        st.warning("No se proporcionó ningún archivo.")
        return

    # Crear archivo temporal con extensión correcta
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio.read())
        input_path = tmp.name

    # Crear otro archivo temporal para el WAV de salida
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_output:
        wav_path = temp_output.name

    # Convertir el archivo MP3 a WAV usando ffmpeg
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", input_path, wav_path], check=True
        )
        st.success("✅ Conversión a WAV completada.")
    except subprocess.CalledProcessError:
        st.error("❌ Error al convertir el archivo a WAV.")
        return

    # Cargar el archivo WAV usando librosa
    try:
        waveform, sr = librosa.load(wav_path, sr=16000)
        duration = librosa.get_duration(y=waveform, sr=sr)
        st.write(f"Duración del archivo: {duration:.2f} segundos")
    except Exception as e:
        st.error(f"❌ Error al cargar el archivo WAV: {e}")
        return

    # Usar el modelo Whisper para la transcripción
    try:
        model = whisper.load_model("small")
        result = model.transcribe(wav_path)
        st.write("Texto transcrito:")
        st.write(result['text'])
    except Exception as e:
        st.error(f"❌ Error al transcribir el archivo: {e}")
