"""Contains english_to_french(english_text) and french_to_english(french_text)."""
from deep_translator import GoogleTranslator
def english_to_french(english_text):
    """Translates from English to French."""
    french_text = GoogleTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Tanslates from French to English."""
    english_text = GoogleTranslator(source='french', target='english').translate(french_text)
    return english_text
