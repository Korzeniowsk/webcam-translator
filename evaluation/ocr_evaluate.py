import json
import time
from datetime import datetime

class OCREvaluator:
    def __init__(self):
        self.results = []

    def calculation_cer(self, truth, predicted):
        len_t = len(truth)
        len_pred = len(predicted)

        dp = [[0] * (len_pred+1) for _ in range (len_t +1)]

        for i in range(len_t + 1):
            dp[i][0] = i
        for j in range (len_t + 1):
            dp[0][j] = j

        for i in range(1, len_t + 1):
            for j in range (1, len_pred + 1):
                if truth[i-1] == predicted[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

            
        edit_distance = dp[len_t][len_pred]
        cer = edit_distance/max(len_t, 1)
        return round(cer,4)
        

    def calculation_wer (self, truth, predicted):
        t_words = truth.split()
        pred_words = predicted.split()

        len_t = len(t_words)
        len_pred = len(pred_words)

        dp = [[0] * (len_pred + 1) for _ in range (len_t + 1)]

        for i in range(len_t + 1 ):
            dp [i][0] = i
        for j in range (len_pred + 1):
            dp [0][j] = j
        
        for i in range (1, len_t + 1):
            for j in range (1, len_t+1):
                if t_words[i-1] == pred_words[j-1]:
                    dp[i][j] == dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        edit_distance = dp[len_t,len_pred]
        wer = edit_distance/max(len_t, 1)
        return(wer,4)


    def log_results (self, truth, predicted, latency_in_ms):

        cer = self.calculation_cer(truth, predicted)
        wer = self.calculation_wer(truth, predicted)

        results = {
            "timestamp": datetime.now().isoformat(),
            "Truth": truth,
            "Predicted": predicted,
            "CER": cer,
            "WER": wer,
            "Latency_in_ms": latency_in_ms
        }
        self.results.append(results)
        return results
    
    def save_report (self, path="evaluation/report.json"):
        if not self.results:
            return
        
        avg_cer = sum(r["cer"] for r in self.results) / len(self.results)
        avg_wer = sum(r["wer"] for r in self.results) / len(self.results)
        avg_latency = sum(r["latency_in_ms"] for r in self.result) / len(self.results)

        report = {
            "Total samples": len(self.results),
            "Average_CER": round(avg_cer, 4),
            "Average_WER": round(avg_wer, 4),
            "Average_latency_in_ms": round(avg_latency, 2),
            "Results": self.results
        }

        with open(path, 'w', encoding ='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent = 2)
        
        print(f"Report saved to {path}")
        print(f"Average CER: {avg_cer:.2%}")
        print(f"Average WER: {avg_wer:.2%}")
        print(f"Average Latency: {avg_latency:.0f}ms")
