import streamlit as st
import requests
from gtts import gTTS
import os
import pykakasi

st.markdown("""
<style>
.stApp {
    background-image: url("https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3YxMTU1LWItMDExLmpwZw.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    color: #2d3436;  /* Makes text white */
}
</style>
""", unsafe_allow_html=True)

# Setup Romaji converter
kks = pykakasi.kakasi()

def to_romaji(text):
    result = kks.convert(text)
    return ''.join([item['hepburn'] for item in result])

def get_word_info(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    response = requests.get(url)
    data = response.json()
    if data['data']:
        entry = data['data'][0]
        japanese = entry['japanese'][0]
        kanji = japanese.get('word', japanese['reading'])
        reading = japanese['reading']
        romaji = to_romaji(reading)
        meaning = ', '.join(entry['senses'][0]['english_definitions'])
        pos = ', '.join(entry['senses'][0]['parts_of_speech'])
        return kanji, reading, romaji, meaning, pos
    else:
        return None, None, None, None, None

# def simple_example(word):
#     return f"{word} が好きです。 (I like {word}.)"

def generate_audio(text, filename='audio.mp3'):
    tts = gTTS(text=text, lang='ja')
    tts.save(filename)


st.title("JLPT Flashcard Generator ")
st.write("Enter a Japanese word and get its details:")

user_input = st.text_input("Japanese word:")

if user_input:
    kanji, reading, romaji, meaning, pos = get_word_info(user_input)

    if kanji:
        st.success(f"**Kanji:** {kanji}")
        st.markdown(f"**Reading (Kana):** {reading}")
        st.markdown(f"**Romaji:** {romaji}")
        st.markdown(f"**Meaning:** {meaning}")
        st.markdown(f"**Part of Speech:** {pos}")

        # Example sentence
        # sentence = simple_example(kanji)
        # st.markdown(f"**Example Sentence:** {sentence}")

        # Audio
        generate_audio(reading)
        st.markdown("Audio")
        st.audio("audio.mp3")


    else:
        st.error(" Word not found. Try a different one.")
