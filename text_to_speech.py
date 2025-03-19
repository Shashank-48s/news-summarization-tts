from gtts import gTTS
from deep_translator import GoogleTranslator

def translate_text(text, target_lang="hi"):
    """
    Translate text to Hindi using Deep Translator.
    :param text: The text to be translated
    :param target_lang: The target language code (default: 'hi' for Hindi)
    :return: Translated text
    """
    translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
    return translated

def convert_text_to_speech(text, filename="output.mp3", lang="hi"):
    """
    Convert translated text to speech and save it as an MP3 file.
    :param text: Text to be converted to speech
    :param filename: Output file name (default: output.mp3)
    :param lang: Language code (default: 'hi' for Hindi)
    """
    translated_text = translate_text(text, lang)  # Translate first
    tts = gTTS(text=translated_text, lang=lang, slow=False)
    tts.save(filename)
    print(f"🔊 Speech saved as {filename}")

# Example usage
if __name__ == "__main__":
    sample_text = "Tesla faces major challenges in the market."
    convert_text_to_speech(sample_text, "tesla_news_hindi.mp3")
