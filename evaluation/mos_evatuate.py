from gtts import gTTS
from playsound import playsound
import tempfile
import os
import json
from datetime import datetime

class MOSEvaluator:
    def __init__(self):
        self.scores=[]

    def evaluate(self, text, lang='hi'):
        tts = gTTS(text=text, lang=lang, slow=False)
        with tempfile.NamedTemporaryFile(delete = False, suffix='.mp3') as f:
            temp_path = f.name
        tts.save(temp_path)

        playsound(temp_path)
        os.remove(temp_path)

        while True:
            try:
                score = int(input(f"Rate the audio quality (1-5): "))
                if 1 <= score <= 5:
                    break
                print("Please enter a number between 1 and 5")
            
            except ValueError:
                print("Invalid input")
        
        self.scores.append({
            "text": text,
            "lang": lang,
            "MOS_score ": score,
            "timestamp": datetime.now().isoformat()
        })
        return score
    
    def save_report(self, path="evaluation/mos_reprot.json"):
        if not self.scores:
            return
        avg_mos = sum(s["mos_score"] for s in self.scores) / len(self.scores)
        report = {
            "Average_mos": round(avg_mos, 2),
            "total_samples": len(self.scores),
            "scores": self.scores
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"Average MOS: {avg_mos:.2f}/5.0")

