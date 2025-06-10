import ollama

def query_llm(prompt: str, model: str = "mistral") -> str:
    try:
        response = ollama.chat(model=model, messages=[
            {"role": "user", "content": prompt}
        ])
        return response["message"]["content"]
    except Exception as e:
        print(f"Error querying LLM ({model}): {e}")
        return ""