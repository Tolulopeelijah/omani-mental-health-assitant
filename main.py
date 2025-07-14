import asyncio
import time
# from audio import record_audio
from stt.convert_text import transcribe_audio
from llm.generator import generate_response
from tts import tts
from tts.utils import save_wav
from logger import SessionLogger

async def run_conversation(audio_path):
    logger = SessionLogger()

    # audio_path = record_audio()

    # Transcribing
    start_time = time.time()
    result = transcribe_audio(audio_path)
    user_text = result["text"]
    print(f"User said: {user_text}")

    # Generate response (LLM)
    response, model_used = await generate_response(user_text, return_model=True)
    print(f"Assistant response ({model_used}): {response}")

    # Convert to speech (TTS)
    audio_path = tts.synthesize(response)
    print(f"Response audio saved at: {audio_path}")


    # Log the turn
    latency = time.time() - start_time
    logger.log_turn(
        asr_output=user_text,
        llm_input=user_text,
        llm_model=model_used,
        llm_response=response,
        tts_path=audio_path,
        latency=latency
    )

for i in range(5):
    asyncio.run(run_conversation(f'data/samples/sample{i}.wav'))

