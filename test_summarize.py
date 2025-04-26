# utils/test/test_summarize.py

import pytest
from utils import summarize

def fake_summarize_text(text: str):
    return "This is a fake summary."

def test_summarize_text(monkeypatch):
    monkeypatch.setattr(summarize, "summarize_text", fake_summarize_text)
    
    result = summarize.summarize_text("Testing input")
    assert result == "This is a fake summary."
