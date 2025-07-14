import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stt.convert_text import transcribe_audio
from llm.generator import generate_response
from tts.tts import synthesize
import asyncio

def test_end_to_end():
    sample_path = "data/samples/sample_arabic.wav"
    if not os.path.exists(sample_path):
        return
    stt_result = transcribe_audio(sample_path)
    user_text = stt_result["text"]
    assert isinstance(user_text, str)
    
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(generate_response(user_text))
    assert isinstance(response, str)
    
    tts_path = "data/log/response_test.wav"
    synthesize(response, output_dir=tts_path)
    assert os.path.exists(tts_path)
