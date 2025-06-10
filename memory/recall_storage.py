"""
recall_storage.py

This module manages session-based long-term memory storage for the MemGPT-inspired system.
Each session has its own recall log saved as a JSON file under `data/recall_sessions/`.

Core Functions:
- save_to_recall(): Append a memory entry
- search_recall(): Search stored entries
- load_recall(): View current recall state
"""

import json
import os
from typing import List
from datetime import datetime

# Create a session ID based on timestamp
SESSION_ID = datetime.now().strftime("%Y%m%d_%H%M%S")
RECALL_DIR = "data/recall_sessions"
os.makedirs(RECALL_DIR, exist_ok=True)

RECALL_FILE = os.path.join(RECALL_DIR, f"{SESSION_ID}.json")

def save_to_recall(entry: str):
    data = load_recall()
    data.append(entry)
    with open(RECALL_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_recall() -> List[str]:
    if not os.path.exists(RECALL_FILE):
        return []
    with open(RECALL_FILE, "r") as f:
        return json.load(f)

def search_recall(keyword: str) -> List[str]:
    data = load_recall()
    return [line for line in data if keyword.lower() in line.lower()]

def clear_recall():
    with open(RECALL_FILE, "w") as f:
        json.dump([], f)