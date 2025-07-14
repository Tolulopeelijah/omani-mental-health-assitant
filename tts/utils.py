# tts/utils.py

import soundfile as sf
import os
from datetime import datetime
import numpy as np

def save_wav(audio_data, sample_rate=22050, save_dir="../data/logs"):
    """
    Save generated audio to a WAV file.

    Args:
        audio_data (np.ndarray): The audio waveform to save.
        sample_rate (int): Sample rate of the audio.
        save_dir (str): Directory to save the audio file.
    Returns:
        str: Full path to the saved WAV file.
    """
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"response_{timestamp}.wav"
    path = os.path.join(save_dir, filename)

    # Ensure audio is at least 2D for compatibility with sf.write
    if isinstance(audio_data, np.ndarray) and audio_data.ndim == 1:
        audio_data = audio_data.reshape(-1, 1)

    sf.write(path, audio_data, sample_rate)
    print(f"Response audio saved to: {path}")
    return path
