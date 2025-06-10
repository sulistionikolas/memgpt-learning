"""
prompt_compiler.py

Constructs the full prompt sent to the LLM, structured by memory tiers:
- System Instructions
- Working Context (historical memory)
- User Input (active query)

This reflects MemGPT's architecture where each memory section is clearly delineated.
"""

from prompt.system_instructions import SYSTEM_INSTRUCTIONS
from memory.context import WorkingContext

def compile_prompt(user_prompt: str, context: WorkingContext) -> str:
    """
    Builds a structured prompt with:
    - System instructions
    - Historical working memory
    - Latest user question
    """
    prompt_parts = [
        "### System Instructions:\\n" + SYSTEM_INSTRUCTIONS.strip(),
        "### Working Context (Memory):\\n" + str(context).strip(),
        "### User Prompt:\\n[User] " + user_prompt.strip()
    ]
    return "\\n\\n".join([part for part in prompt_parts if part])