from openai import AsyncOpenAI
import anthropic
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize clients
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = anthropic.AsyncAnthropic(api_key=os.getenv("CLAUDE_API_KEY"))

# Models
GPT_MODEL = "gpt-4o"
CLAUDE_MODEL = "claude-opus-4-20250514"

# GPT Generator (using new OpenAI SDK syntax)
async def generate_with_gpt(prompt: str) -> str:
    try:
        response = await openai_client.chat.completions.create(
            model=GPT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            timeout=7  # seconds
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("GPT-4o failed:", e)
        

# Claude Generator
async def generate_with_claude(prompt: str) -> str:
    try:
        response = await anthropic_client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
    except Exception as e:
        print("Claude failed:", e)
        return "عذرًا، حدث خطأ أثناء إنشاء الرد."  # fallback response

USE_DUMMY_MODE = False
async def generate_response(prompt: str, return_model=False) -> str | tuple[str, str]:

    if USE_DUMMY_MODE:
        dummy_response = "هذا رد تجريبي من المساعد لتوفير التوكنات أثناء الاختبار."
        return (dummy_response, "dummy") if return_model else dummy_response


    try:
        response = await asyncio.wait_for(generate_with_gpt(prompt), timeout=15)
        return (response, "gpt-4o") if return_model else response
    except Exception as e:
        print("Falling back to Claude...")
        response = await generate_with_claude(prompt)
        return (response, "claude-opus") if return_model else response

# # for testing
# if __name__ == "__main__":
#     async def test():
#         prompt = "مرحباً، كيف حالك اليوم؟"
#         response = await generate_response(prompt)
#         print(" Prompt:", prompt)
#         print(" Response:", response)

#     asyncio.run(test())
