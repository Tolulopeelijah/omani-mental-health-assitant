# audio/noise_reduction.py

import noisereduce as nr
import soundfile as sf
import numpy as np
import os

def reduce_noise(input_path, output_path=None, use_static_noise_profile=False):
    """
    Apply noise reduction to an audio file.

    Args:
        input_path (str): Path to input .wav file.
        output_path (str): Where to save cleaned audio. If None, it won't save.
        use_static_noise_profile (bool): Whether to estimate noise from first 0.5s.

    Returns:
        np.ndarray: Cleaned audio signal.
        int: Sampling rate
    """
    try:
        audio_data, sr = sf.read(input_path)
        
        if use_static_noise_profile:
            # Use the first 0.5 seconds as noise sample
            noise_sample = audio_data[:int(0.5 * sr)]
            reduced_audio = nr.reduce_noise(y=audio_data, y_noise=noise_sample, sr=sr)
        else:
            # Automatically estimate noise
            reduced_audio = nr.reduce_noise(y=audio_data, sr=sr)

        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            sf.write(output_path, reduced_audio, sr)
            print(f"✅ Cleaned audio saved to: {output_path}")

        return reduced_audio, sr

    except Exception as e:
        print(f"❌ Noise reduction failed: {e}")
        return None, None

# Example usage:
# reduce_noise("data/samples/audio_20250708_1030.wav", "data/samples/cleaned_audio.wav")
