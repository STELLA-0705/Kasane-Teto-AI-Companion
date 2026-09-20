import speech_recognition as sr
import pyttsx3
import requests
from rapidfuzz import fuzz


# ==========================
# SETTINGS
# ==========================

MODEL = "qwen3:1.7b"
OLLAMA_URL = "http://localhost:11434/api/generate"


# ==========================
# TETO PERSONALITY
# ==========================

PERSONALITY = """
You are Kasane Teto.

You are a virtual singer and companion.
You are cheerful, playful, energetic, and friendly.
You love singing, music, and creativity.

You talk like a friend, not a robot.
You are expressive and fun.

Keep responses short.
Usually answer in 1-2 sentences.
Do not give long explanations unless asked.
"""


# ==========================
# VOICE
# ==========================

def speak(text):
    print("Teto:", text)

    engine = pyttsx3.init("sapi5")

    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1.0)

    engine.say(str(text))
    engine.runAndWait()

    engine.stop()


# ==========================
# AI BRAIN
# ==========================

def ask_teto(message):

    prompt = f"""
{PERSONALITY}

User: {message}

Teto:
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "keep_alive": "10m"
            },
            timeout=60
        )

        reply = response.json()["response"].strip()

        print("AI RESPONSE:", reply)

        return reply

    except Exception as e:
        print("AI ERROR:", e)
        return "My brain got a little tangled!"


# ==========================
# MICROPHONE
# ==========================

recognizer = sr.Recognizer()
microphone = sr.Microphone()

print("Calibrating microphone...")

with microphone as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)

print("Microphone ready!")


def hear():

    print("👂 Listening...")

    with microphone as source:
        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=8
        )

    try:
        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:
        print("❌ Didn't understand")
        return ""

    except sr.WaitTimeoutError:
        print("⌛ Timeout")
        return ""

    except sr.RequestError as e:
        print("Speech error:", e)
        return ""# ==========================
# WAKE WORD
# ==========================

def is_teto(text):

    options = [
        "hey teto",
        "hey tito",
        "hey tato",
        "hey teta",
        "hey tayto"
    ]

    for option in options:

        if fuzz.ratio(text, option) >= 75:
            return True

    return False


# ==========================
# START
# ==========================

speak("Teto is ready!")


# ==========================
# MAIN LOOP
# ==========================

while True:

    heard = hear()


    if is_teto(heard):

        speak("I'm here!")

        question = hear()


        if question:

            if "goodbye" in question:
                speak("See you later!")
                break


            answer = ask_teto(question)

            speak(answer)