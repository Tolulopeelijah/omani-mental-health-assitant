import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tts.tts import synthesize

def test_text_to_speech_creates_file():
    path = "data/logs/response_test.wav"
    synthesize("مرحبا بك", output_dir=path)
    assert os.path.exists(path)
