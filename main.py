"""
main.py

CLI-based MemGPT simulation with improved prompt readability.
Injects system instructions, working context, and FIFO queue into the LLM prompt.
Handles memory updates and function calls.
"""

from llm_interface import query_llm
from memory.working_context import WorkingContext
from memory.fifo_queue import FIFOQueue
from memory.recall_storage import save_to_recall, load_recall
from core.function_executor import execute_function
from prompt.prompt_compiler import compile_prompt

# Init memory objects
working_context = WorkingContext()
fifo_queue = FIFOQueue(max_turns=10)

def handle_interaction(prompt: str):
    if prompt.strip().startswith("{") and "function" in prompt:
        try:
            import json
            func_call = json.loads(prompt)
            result = execute_function(func_call, working_context)
            print("\n🛠️ Function Output:")
            print(result)
            print("-" * 60)
            return
        except Exception as e:
            print(f"❌ Failed to parse function call: {e}")
            return

    # Add user input to FIFO
    fifo_queue.add_turn("user", prompt)

    # Compile structured prompt
    full_prompt = compile_prompt(prompt, working_context, fifo_queue)
    response = query_llm(full_prompt).strip().replace("\n", " ").replace("  ", " ")

    # Add assistant response to FIFO
    fifo_queue.add_turn("assistant", response)

    # Print memory state
    print("\n🧠 Working Context:")
    print(working_context.get_prompt_text())

    print("\n🔁 FIFO Queue (Recent Conversation):")
    print(fifo_queue.get_prompt_text())

    print("\n📦 Recall Memory:")
    print(load_recall())
    print("-" * 60)

if __name__ == "__main__":
    print("🧪 MemGPT Local Simulator (CTRL+C to exit)")
    try:
        while True:
            user_input = input("\nYou > ")
            handle_interaction(user_input)
    except KeyboardInterrupt:
        print("\n👋 Exiting. Session saved.")