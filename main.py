import streamlit as st
from googletrans import Translator
from PyPDF2 import PdfReader
import json

# Load languages from config.json
with open('config.json', 'r') as file:
    config = json.load(file)

languages = config['languages']

def translate_pdf(pdf_file, src_lang, dest_lang):
    reader = PdfReader(pdf_file)
    translator = Translator()
    translated_text = ""
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            translated = translator.translate(text, src=src_lang, dest=dest_lang)
            translated_text += translated.text + "\n"
    
    return translated_text

st.title("PDF Translator")

src_lang_name = st.selectbox("Source Language", list(languages.keys()))
dest_lang_name = st.selectbox("Destination Language", list(languages.keys()))

src_lang = languages[src_lang_name]
dest_lang = languages[dest_lang_name]

pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file and st.button("Translate"):
    with st.spinner("Translating..."):
        translated_text = translate_pdf(pdf_file, src_lang, dest_lang)
        st.text_area("Translated Text", value=translated_text, height=400)
