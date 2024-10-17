import streamlit as st
from audiogen import generate_audio_array
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import lyricgen

st.title("Mood to Music Converter")

mood = st.text_input("Enter your mood: ", placeholder = "e.g Happy, Sad, Excited")
genre = st.text_input("Choose your genre: ", placeholder = "e.g. Pop, Rock, Jazz")
vibe = st.text_input("Enter a vibe: ", placeholder = "e.g. Upbeat, Empowering, Depressing")
subject = st.text_input("Decide on a subject or theme: ", placeholder = "e.g. Love, Adventure, Friendship")
keywords = st.text_input("Enter one or more keywords separated by commas: ", placeholder = "e.g. Night, Happy, Alone")

if st.button("Generate and Play Audio"):
    user_input = f"Mood: {mood}, Genre: {genre}, Vibe: {vibe}, Subject: {subject}, Keywords: {keywords}\n"
    lyric = lyricgen.generate_prompt(user_input)
    st.write("## Generated Lyric:")
    st.write(lyric)
    audio_array = generate_audio_array(lyric) 
    st.audio(data=audio_array, sample_rate=SAMPLE_RATE)
