"""
function_executor.py

Dispatches LLM-generated function calls to real implementations.
Currently supports updating and retrieving working context.
"""

from memory.working_context import WorkingContext
from memory.recall_storage import search_recall

def execute_function(call: dict, working_context: WorkingContext) -> str:
    func = call.get("function")
    
    if func == "update_working_context":
        key = call.get("key")
        value = call.get("value")
        if not key or not value:
            return "❌ Missing 'key' or 'value' in update_working_context"
        working_context.set_fact(key, value)
        return f"✅ Working context updated: {key} = {value}"

    elif func == "get_working_context":
        return working_context.get_prompt_text()

    elif func == "search_recall":
        keyword = call.get("keyword")
        if not keyword:
            return "❌ Missing 'keyword' in search_recall"
        results = search_recall(keyword)
        return "\\n".join(results) if results else "No relevant recall entries found."

    return f"❌ Unknown function: {func}"