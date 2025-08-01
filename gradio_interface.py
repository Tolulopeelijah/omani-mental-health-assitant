import gradio as gr
import tempfile
import asyncio
import time
import scipy.io.wavfile

from stt.convert_text import transcribe_audio
from llm.generator import generate_response
from tts import tts
from logger import SessionLogger 


# Initialize logger (one per session)
logger = SessionLogger(log_dir="data/logs") 

# Helper: End-to-end processing function
def process_audio(audio):
    if not audio:
        return "لم يتم تسجيل الصوت.", None

    sample_rate, audio_data = audio

    # Save audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        scipy.io.wavfile.write(tmp_file.name, sample_rate, audio_data)
        audio_path = tmp_file.name

    start_time = time.time()

    # Step 1: ASR
    stt_result = transcribe_audio(audio_path)
    user_text = stt_result["text"]

    # Step 2: LLM with fallback
    response, model_used = asyncio.run(generate_response(user_text, return_model=True))

    # Step 3: TTS
    audio_response = tts.synthesize(response)

    latency = time.time() - start_time

    # Save audio response to file to get a path for logging (optional)
    response_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    scipy.io.wavfile.write(response_path, tts.sample_rate, audio_response)

    # Step 4: Logging
    logger.log_turn(
        asr_output=user_text,
        llm_input=user_text,
        llm_model=model_used,
        llm_response=response,
        tts_path=response_path,
        latency=latency
    )

    # Final display
    return f"المستخدم: {user_text}\n المساعد: {response}", (tts.sample_rate, audio_response)


# Launch Gradio Interface
gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(sources="microphone", type="numpy", label="تحدث الآن (عربية عمانية)"),
    outputs=[
        gr.Text(label="نص المحادثة"),
        gr.Audio(type="numpy", label="رد المساعد")
    ],
    title="المساعد الصوتي للصحة النفسية - العربية العمانية",
    description="هذا المساعد يستمع إليك، يرد باستخدام GPT-4o (مع دعم احتياطي لـ Claude)، ويتحدث باللهجة العمانية.",
    live=True,
    theme="default",
).launch()