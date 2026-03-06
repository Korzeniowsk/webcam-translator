from deep_translator import GoogleTranslator
from config import TARGET_LANGUAGE

class TextTranslator:
    def __init__(self):
        self.translator = GoogleTranslator(source="auto", target=TARGET_LANGUAGE)
        self.last_text = "" #This is to avoid translating one text multiple times

    def translate (self, text):
        if not text or text == self.last_text:
            return None
        
        try:
            translated = self.translator.translate(text)
            self.last_text = text
            return translated
        except Exception as e:
            print(f"Translation error, sorry: {e}")
            return None