import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stt.convert_text import transcribe_audio

def test_transcribe_audio_returns_dict():
    sample_path = "data/samples/sample_arabic.wav"
    if not os.path.exists(sample_path):
        # Skip test if sample audio is not available
        return
    result = transcribe_audio(sample_path)
    assert isinstance(result, dict)
    assert "text" in result
