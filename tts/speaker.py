from gtts import gTTS
from playsound import playsound
import tempfile
import os
from config import TTS_LANGUAGE

class Speaker:
    def speak(self, text):
        if not text:
            return
        
        try:
            tts=gTTS( text= text, lang=TTS_LANGUAGE, slow=False)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
                temp_path = f.name
            
            tts.save(temp_path)
            playsound(temp_path)
            os.remove(temp_path)
        
        except Exception as e:
            print(f"TTS error, sorry!: {e}")

