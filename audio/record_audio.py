import sounddevice as sd
import soundfile as sf
import numpy as np
import os
from datetime import datetime

def record_audio(filename="output.wav", duration=5, samplerate=16000, channels=1, save_dir="data/samples"):
    """
    Records audio from the default microphone and saves it to a .wav file.
    
    Args:
        filename (str): Name of the output file.
        duration (int): Duration of the recording in seconds.
        samplerate (int): Sampling rate in Hz.
        channels (int): Number of channels (1 = mono, 2 = stereo).
        save_dir (str): Directory to save the audio file.

    Returns:
        np.ndarray: The recorded audio as a NumPy array.
    """
    os.makedirs(save_dir, exist_ok=True)
    full_path = os.path.join(save_dir, filename)

    print(f"🎙️ Recording for {duration} seconds...")

    try:
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate,
                       channels=channels, dtype='float32')
        sd.wait()  # Wait until recording is finished
        sf.write(full_path, audio, samplerate)
        print(f"✅ Saved to {full_path}")
        return audio
    except Exception as e:
        print(f"❌ Recording failed: {e}")
        return None

def generate_timestamped_filename(prefix="audio"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.wav"

# Example usage (uncomment to test):
# if __name__ == "__main__":
#     fname = generate_timestamped_filename()
#     audio_data = record_audio(filename=fname, duration=4)
