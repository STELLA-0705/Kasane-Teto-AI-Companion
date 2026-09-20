import requests
import config


with open(r"C:\Users\janey\OneDrive\Desktop\Teto AI Companion\Teto_Brain.py", "r", encoding="utf8") as f:
    PERSONALITY = f.read()


def ask(message):

    prompt = f"""
{PERSONALITY}

User: {message}

Teto:
"""

    response = requests.post(
        config.OLLAMA_URL,
        json={
            "model": config.MODEL,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "10m"
        }
    )

    return response.json()["response"].strip()