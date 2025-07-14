import json
import os
from datetime import datetime

class SessionLogger:
    def __init__(self, log_dir="data/logs", session_id=None):
        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir
        self.session_id = session_id or datetime.now().strftime("session_%Y%m%d_%H%M%S")
        self.session_path = os.path.join(log_dir, f"{self.session_id}.json")
        self.log_data = {
            "session_id": self.session_id,
            "turns": []
        }

    def log_turn(self, asr_output, llm_input, llm_model, llm_response, tts_path, latency):
        turn = {
            "timestamp": datetime.now().isoformat(),
            "asr_output": asr_output,
            "llm_input": llm_input,
            "llm_model": llm_model,
            "llm_response": llm_response,
            "tts_path": tts_path,
            "latency_seconds": round(latency, 2)
        }
        self.log_data["turns"].append(turn)
        self._save()

    def _save(self):
        with open(self.session_path, "w", encoding="utf-8") as f:
            json.dump(self.log_data, f, ensure_ascii=False, indent=2)
