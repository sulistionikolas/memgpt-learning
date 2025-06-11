"""
prompt_compiler.py

Constructs the full prompt to be sent to the LLM using structured memory tiers:
- Static system instructions
- Working context (editable facts)
- FIFO queue (short-term message history)
- User input (latest query)
"""

from prompt.system_instructions import SYSTEM_INSTRUCTIONS
from memory.working_context import WorkingContext
from memory.fifo_queue import FIFOQueue

def compile_prompt(user_prompt: str, working_context: WorkingContext, fifo_queue: FIFOQueue) -> str:
    """
    Builds a complete structured prompt with all memory tiers.
    """
    sections = [
        "### System Instructions\\n" + SYSTEM_INSTRUCTIONS.strip(),
        "### Working Context (Editable Facts)\\n" + working_context.get_prompt_text(),
        "### FIFO Queue (Conversation History)\\n" + fifo_queue.get_prompt_text(),
        "### User Prompt\\n[User] " + user_prompt.strip()
    ]
    return "\\n\\n".join(sections)