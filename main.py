import asyncio
import time
# from audio import record_audio
from stt.convert_text import transcribe_audio
from llm.generator import generate_response
from tts import tts
from tts.utils import save_wav
from logger import SessionLogger

latencies = {}
async def run_conversation(audio_path):
    logger = SessionLogger()

    # audio_path = record_audio()
    total_start_time = time.time()
    # Transcribing
    start_time = time.time()
    result = transcribe_audio(audio_path)
    user_text = result["text"]
    print(f"User said: {user_text}")

    latency = time.time() - start_time
    latencies['transcribe'] = round(latency, 2)

    # Generate response (LLM)
    start_time = time.time()
    response, model_used = await generate_response(user_text, return_model=True)
    print(f"Assistant response ({model_used}): {response}")

    latency = time.time() - start_time
    latencies['llm'] = round(latency, 2)

    # Convert to speech (TTS)
    start_time = time.time()
    audio_path = tts.synthesize(response)
    print(f"Response audio saved at: {audio_path}")


    latency = time.time() - start_time
    latencies['tts'] = round(latency, 2)

    latencies['total'] = round(time.time() - total_start_time, 2)
    logger.log_turn(
        asr_output=user_text,
        llm_input=user_text,
        llm_model=model_used,
        llm_response=response,
        tts_path=audio_path,
        latencies=latencies
    )

for i in range(5):
    asyncio.run(run_conversation(f'data/samples/sample{i}.wav'))

