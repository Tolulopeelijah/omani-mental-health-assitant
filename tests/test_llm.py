import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from llm.generator import generate_response
import asyncio

@pytest.mark.asyncio
async def test_generate_response_returns_text():
    prompt = "مرحباً، كيف حالك اليوم؟"
    result = await generate_response(prompt)
    assert isinstance(result, str)
    assert len(result.strip()) > 0
