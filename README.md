# 🧠 Omani Arabic Mental Health Voice Assistant

A culturally adapted, voice-enabled mental health support assistant designed for Arabic speakers in Oman. It uses speech recognition, large language models (GPT-4o and Claude Opus), and text-to-speech to provide empathetic, non-judgmental responses in Omani Arabic.

---

## 📌 Features

- 🎤 **Voice Input**: Users speak directly into the app.
- 🧠 **Dual LLMs**: Uses GPT-4o as the main model with Claude Opus as fallback.
- 🗣️ **Voice Output**: Natural, supportive Arabic responses using gTTS.
- 🕌 **Cultural Sensitivity**: Designed to align with Islamic values, Omani dialect, and mental health etiquette.
- 📚 **Logging & Evaluation**: Keeps track of transcripts, model usage, and latency for analysis.

---

## 🧰 Tech Stack

| Component           | Technology                  |
|--------------------|-----------------------------|
| Speech-to-Text     | [FasterWhisper](https://github.com/guillaumekln/faster-whisper) |
| Language Models    | GPT-4o (OpenAI), Claude 3 Opus (Anthropic) |
| Text-to-Speech     | [gTTS](https://pypi.org/project/gTTS/) |
| Interface          | [Gradio](https://www.gradio.app/) |
| Logging            | JSON file-based logging |
| Language           | Python 3.10+ |

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/omani-mental-health-assistant.git
   cd omani-mental-health-assistant
Create Environment

bash
Copy
Edit
conda create -n omani_mental_agent python=3.10
conda activate omani_mental_agent
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set API Keys

Create a .env file in the root directory with your credentials:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-key
CLAUDE_API_KEY=your-anthropic-key
Run the App

bash
Copy
Edit
python app.py
This launches the Gradio interface for real-time voice interaction.

🧪 Testing
Unit and integration tests are located in the tests/ directory.

Run all tests:

bash
Copy
Edit
pytest tests/
📁 Project Structure
bash
Copy
Edit
.
├── app.py                  # Gradio interface
├── main.py                 # CLI-based pipeline runner
├── llm/
│   └── generator.py        # Handles GPT & Claude fallback logic
├── stt/
│   └── recognizer.py       # FasterWhisper transcription
├── tts/
│   ├── tts_engine.py       # gTTS engine
│   └── utils.py            # Audio saving utilities
├── data/
│   ├── logs/               # Generated logs (JSON + audio)
│   └── samples/            # Sample inputs
├── logger/
│   └── logger.py           # Handles JSON logging per interaction
├── .env                    # API keys
└── requirements.txt
🛡️ Safety & Ethics
Suicide risk escalation triggers (future scope).

Cultural appropriateness checked through prompt design.

No storage of sensitive data without consent.

Responses avoid hallucinations via prompt constraints and fallback monitoring.

📈 Performance
Average GPT-4o latency: ~3.5s (may vary due to network).

Claude Opus used if timeout exceeds 8–10s.

Logs saved for every interaction.

🧭 Future Roadmap
Deploy to cloud server with Docker support.

Integrate real-time escalation and referral systems.

Fine-tune Arabic LLM for offline use.

Expand dialect support beyond Omani Arabic.

Demo Video
Watch the Demo (YouTube Link)