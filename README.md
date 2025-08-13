# JLPT-smartcard-generator
JLPT Flashcard Generator is a Streamlit-based web application designed to help Japanese language learners prepare for JLPT (Japanese Language Proficiency Test) levels by generating quick and interactive flashcards.
Users can enter any Japanese word, and the app fetches the following details in real-time:
Kanji and Kana (reading)
Romaji (romanized reading)
English meanings
The app uses the Jisho.org API to retrieve word data and converts readings to Romaji using the pykakasi library. It's a lightweight, fast, and visually engaging tool ideal for N5–N3 JLPT learners or casual Japanese language enthusiasts.
Deployed with AWS EC2 for the application backend and S3 + CloudFront for fast content delivery.

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py
