"""
main.py

CLI-based event loop for interacting with a MemGPT-style system.
Injects system instructions and working memory into LLM prompt.
Handles eviction and recall memory.
"""

from llm_interface import query_llm
from memory.context import WorkingContext
from memory.recall_storage import save_to_recall, load_recall
from core.function_executor import execute_function
from prompt.prompt_compiler import compile_prompt

MAX_CONTEXT_SIZE = 5
context = WorkingContext(max_size=MAX_CONTEXT_SIZE)

def handle_interaction(prompt: str):
    if prompt.strip().startswith("{") and "function" in prompt:
        try:
            import json
            func_call = json.loads(prompt)
            result = execute_function(func_call)
            print("🔧 Function Result:")
            print(result)
            return
        except Exception as e:
            print(f"❌ Failed to parse function call: {e}")
            return

    # 🔁 Use prompt compiler to build full LLM prompt
    full_prompt = compile_prompt(prompt, context)
    response = query_llm(full_prompt)

    # Add both prompt and response to working memory
    for item in [f"[User] {prompt}", f"[LLM] {response}"]:
        if len(context.get_context()) >= context.max_size:
            evicted = context.get_context()[0]
            save_to_recall(evicted)
        context.add(item)

    # Print memory state
    print("🧠 Working Context:")
    print(context)
    print("\\n📁 Recall Memory:")
    print(load_recall())

if __name__ == "__main__":
    print("🧪 MemGPT Local Simulator (CTRL+C to exit)")
    try:
        while True:
            prompt = input("\\nYou > ")
            handle_interaction(prompt)
    except KeyboardInterrupt:
        print("\\n👋 Exiting. Session saved.")
