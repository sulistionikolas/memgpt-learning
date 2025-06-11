"""
fifo_queue.py

Manages short-term memory (FIFO message history) within a single session.
This represents MemGPT's rolling message window used for continuity in chat.

Not persisted across sessions.
"""

from typing import List

class FIFOQueue:
    def __init__(self, max_turns: int = 20):
        self.max_turns = max_turns
        self.history: List[str] = []

    def add_turn(self, role: str, message: str):
        entry = f"[{role.capitalize()}] {message.strip()}"
        self.history.append(entry)
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_prompt_text(self) -> str:
        if not self.history:
            return "(no recent messages)"
        return "\\n".join([f"* {line}" for line in self.history])

    def clear(self):
        self.history = []