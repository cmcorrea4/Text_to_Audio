import streamlit as st
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio

# Función para convertir texto en audio
def text_to_speech(text):
    tts = gTTS(text)
    fp = BytesIO()
    tts.save(fp)
    return fp

# Interfaz de usuario
st.title("Convertir texto en audio")

# Ingresar el texto
text = st.text_area("Ingrese el texto que desea convertir en audio")

# Botón para convertir el texto en audio
if st.button("Convertir"):
    if text:
        audio = text_to_speech(text)
        st.audio(audio)
    else:
        st.warning("Por favor ingrese un texto")
