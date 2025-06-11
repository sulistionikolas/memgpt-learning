"""
working_context.py

Structured memory manager for editable key-value facts about the user or session.
Represents the "Working Context" in MemGPT — injected into every prompt, persists across sessions.
"""

import os
import json
from typing import Dict

DEFAULT_PATH = "../data/memory_store/working_context.json"

class WorkingContext:
    def __init__(self, path: str = DEFAULT_PATH):
        self.path = path
        self.memory: Dict[str, str] = {}
        self.load()

    def set_fact(self, key: str, value: str):
        self.memory[key] = value
        self.save()

    def remove_fact(self, key: str):
        if key in self.memory:
            del self.memory[key]
            self.save()

    def clear(self):
        self.memory = {}
        self.save()

    def get_prompt_text(self) -> str:
        if not self.memory:
            return "(no known working context)"
        return "\\n".join([f"- {k.replace('_', ' ').capitalize()}: {v}" for k, v in self.memory.items()])

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=2)

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}