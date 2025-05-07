import streamlit as st
import sys
import subprocess
import librosa
import whisper
import io
import streamlit as st
import whisper
import librosa
import io
import subprocess
import os
import tempfile

def procesar_audio(audio):
    if audio is None:
        st.warning("No se proporcionó ningún archivo.")
        return

    # Crear archivo temporal con extensión correcta
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio.read())
        input_path = tmp.name

    # Convertir a WAV (por ejemplo si fuera mp3)
    wav_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    subprocess.run(["ffmpeg", "-y", "-i", input_path, wav_path], check=True)

    # Cargar con librosa
    waveform, sr = librosa.load(wav_path, sr=16000)
    duration = librosa.get_duration(y=waveform, sr=sr)

    # Transcribir con Whisper
    model = whisper.load_model("small")
    result = model.transcribe(wav_path, word_timestamps=True)

    # Mostrar la transcripción
    transcripcion = ""
    for segment in result['segments']:
        for word in segment['words']:
            transcripcion += f"{word['word']} - start: {word['start']:.2f}s, end: {word['end']:.2f}s\n"

    st.text("Transcripción completada.")
    st.text(f"Duración del audio: {duration:.2f} segundos")
    st.text("Transcripción del audio:")
    st.text(transcripcion)

    # Opcional: limpiar archivos temporales
    os.remove(input_path)
    os.remove(wav_path)
