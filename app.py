from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "StutisResume.pdf"
profile_pic = current_dir / "Assets" / "Photo.jpg"

## Details

PAGE_TITLE = "Digital CV | Stuti Nigam"
PAGE_ICON = ":wave:"
NAME = "Stuti Nigam"
Description = """
Seeking Internship opportunities in Software Engineering starting summer '23.
"""
EMAIL = "stuti2001nigam@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://github.com/stutinigam61",
    "GitHub": "https://www.linkedin.com/in/stutinigam/"
}

PROJECTS = {
    "🏆 Real/fake news bot (A chatbot in Python) - A multi-feature telegram chat bot to predict real or fake news based on the dataset provided.": "https://github.com/stutinigam61/CoreRadioScraper.git",
    "🏆 PlusBackupFiles (Downloader and Uploader in Python) - A multi-file, serial uploader and downloader with combination of command line UI and tkinter GUI." : "https://github.com/stutinigam61/CoreRadioScraper.git",
    "🏆 CoreRadioScraper (scraper in Python) - Scrapes coreradio.ru website for song names and their download links.": "https://github.com/stutinigam61/CoreRadioScraper.git" 
}

st.set_page_config(page_title= PAGE_TITLE, page_icon= PAGE_ICON)

st.title("Hello there")


# LOAD CSS, PDF, PHOTO

with open(css_file) as f:
    st.markdown("<style>{}</srtyle>".format(f.read()), unsafe_allow_html=True)
    








