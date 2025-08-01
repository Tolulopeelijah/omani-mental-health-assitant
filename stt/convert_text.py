from faster_whisper import WhisperModel
import os


MODEL_SIZE = "tiny"  
LANGUAGE_CODE = "ar"  # Arabic

# Loading the model
print("Loading ASR model...")
model = WhisperModel(MODEL_SIZE, compute_type="int8")  # use "int8" for speed
print("ASR model loaded.")

def transcribe_audio(audio_path: str) -> dict:
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    print(f"Transcribing: {audio_path}")

    # Transcribe and get segments
    segments, info = model.transcribe(audio_path, language=LANGUAGE_CODE)

    full_text = ""
    all_segments = []
    for segment in segments:
        start = round(segment.start, 2)
        end = round(segment.end, 2)
        text = segment.text.strip()
        all_segments.append({
            "start": start,
            "end": end,
            "text": text
        })
        full_text += text + " "

    print(f"📝 Transcription: {full_text.strip()}")
    return {
        "text": full_text.strip(),
        "segments": all_segments,
        "language": info.language 
    }


# Test example
if __name__ == "__main__":
    wav_path = "../data/logs/response.wav"
    result = transcribe_audio(wav_path)
    print("[FINAL TEXT]", result["text"])

