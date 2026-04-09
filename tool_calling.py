import requests
import json

def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",   # use lightweight model
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    full_response = ""

    for line in response.iter_lines():
        if line:
            chunk = json.loads(line.decode("utf-8"))
            
            if "response" in chunk:
                print(chunk["response"], end="", flush=True)  # live output
                full_response += chunk["response"]

    return full_response

ask_llm("What's the latest on the Mars rover?")