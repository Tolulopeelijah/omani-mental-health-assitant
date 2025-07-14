# audio/vad.py

import webrtcvad
import collections
import contextlib
import wave
import os
import numpy as np
import soundfile as sf
from scipy.signal import resample

FRAME_DURATION = 30  # ms
SAMPLE_RATE = 16000  # Hz
BYTES_PER_SAMPLE = 2  # 16-bit audio

def read_wave(path):
    audio, sr = sf.read(path)
    
    # Convert stereo to mono
    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    # Resample to 16kHz if needed
    if sr != SAMPLE_RATE:
        audio = resample(audio, int(len(audio) * SAMPLE_RATE / sr))

    # Normalize and convert to int16
    audio = (audio * 32767).astype(np.int16)
    return audio.tobytes(), SAMPLE_RATE

def frame_generator(frame_duration_ms, audio, sample_rate):
    n = int(sample_rate * (frame_duration_ms / 1000.0) * BYTES_PER_SAMPLE)
    offset = 0
    while offset + n < len(audio):
        yield audio[offset:offset + n]
        offset += n

def vad_collector(sample_rate, frame_duration_ms, padding_ms, vad, frames):
    num_padding_frames = int(padding_ms / frame_duration_ms)
    ring_buffer = collections.deque(maxlen=num_padding_frames)
    triggered = False

    voiced_frames = []

    for frame in frames:
        is_speech = vad.is_speech(frame, sample_rate)

        if not triggered:
            ring_buffer.append(frame)
            num_voiced = sum([vad.is_speech(f, sample_rate) for f in ring_buffer])
            if num_voiced > 0.9 * ring_buffer.maxlen:
                triggered = True
                voiced_frames.extend(ring_buffer)
                ring_buffer.clear()
        else:
            voiced_frames.append(frame)
            ring_buffer.append(frame)
            num_unvoiced = sum([not vad.is_speech(f, sample_rate) for f in ring_buffer])
            if num_unvoiced > 0.9 * ring_buffer.maxlen:
                triggered = False
                yield b"".join(voiced_frames)
                ring_buffer.clear()
                voiced_frames = []

    if voiced_frames:
        yield b"".join(voiced_frames)

def save_voiced_segments(input_path, output_dir="data/samples/vad_segments", aggressiveness=2):
    os.makedirs(output_dir, exist_ok=True)

    audio, sample_rate = read_wave(input_path)
    vad = webrtcvad.Vad(aggressiveness)

    frames = list(frame_generator(FRAME_DURATION, audio, sample_rate))
    segments = vad_collector(sample_rate, FRAME_DURATION, padding_ms=300, vad=vad, frames=frames)

    output_files = []
    for i, segment in enumerate(segments):
        segment_path = os.path.join(output_dir, f"segment_{i+1}.wav")
        with wave.open(segment_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(BYTES_PER_SAMPLE)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(segment)
        output_files.append(segment_path)

    print(f"✅ Saved {len(output_files)} speech segment(s) to {output_dir}")
    return output_files

# Example usage:
# if __name__ == "__main__":
#     save_voiced_segments("data/samples/audio_20250708_1030.wav")
