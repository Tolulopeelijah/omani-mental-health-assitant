import sounddevice as sd
import numpy as np
import wave
import time

# Parameters
DURATION = 5  # seconds
SAMPLE_RATE = 16000  # 16kHz for ASR compatibility
CHANNELS = 1
FILENAME = "recorded_audio.wav"

def record_audio(filename=FILENAME, duration=DURATION, fs=SAMPLE_RATE):
    print(f"🎤 Recording for {duration} seconds...")

    # Record audio from the mic
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=CHANNELS, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save as WAV
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit = 2 bytes
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())

    print(f"✅ Audio saved to: {filename}")
    return filename


# Test run
if __name__ == "__main__":
    record_audio()
