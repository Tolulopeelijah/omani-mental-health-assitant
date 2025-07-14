# audio/formats.py

import numpy as np
from scipy.signal import resample

def stereo_to_mono(audio: np.ndarray) -> np.ndarray:
    """
    Converts stereo audio to mono by averaging channels.
    
    Args:
        audio (np.ndarray): Audio array with shape (n_samples,) or (n_samples, 2)

    Returns:
        np.ndarray: Mono audio with shape (n_samples,)
    """
    if audio.ndim == 2:
        return np.mean(audio, axis=1)
    return audio

def normalize(audio: np.ndarray) -> np.ndarray:
    """
    Normalize the audio signal to be in range [-1, 1].

    Args:
        audio (np.ndarray): Input audio waveform

    Returns:
        np.ndarray: Normalized audio
    """
    max_val = np.max(np.abs(audio))
    if max_val == 0:
        return audio
    return audio / max_val

def resample_audio(audio: np.ndarray, original_sr: int, target_sr: int) -> np.ndarray:
    """
    Resample audio to a new sample rate.

    Args:
        audio (np.ndarray): Input waveform
        original_sr (int): Original sampling rate
        target_sr (int): Desired sampling rate

    Returns:
        np.ndarray: Resampled audio waveform
    """
    if original_sr == target_sr:
        return audio
    num_samples = int(len(audio) * float(target_sr) / original_sr)
    return resample(audio, num_samples)

def float32_to_int16(audio: np.ndarray) -> np.ndarray:
    """
    Converts float32 audio (-1.0 to 1.0) to int16 format.

    Args:
        audio (np.ndarray): Float audio waveform

    Returns:
        np.ndarray: Int16 audio waveform
    """
    audio = np.clip(audio, -1.0, 1.0)  # ensure no overflow
    return (audio * 32767).astype(np.int16)

def int16_to_float32(audio: np.ndarray) -> np.ndarray:
    """
    Converts int16 audio to float32 format in range [-1.0, 1.0].

    Args:
        audio (np.ndarray): Int16 waveform

    Returns:
        np.ndarray: Float32 waveform
    """
    return audio.astype(np.float32) / 32767
