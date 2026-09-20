import speech_recognition as sr
import pyttsx3
import requests
import time


# ---------- TETO PERSONALITY ----------

PERSONALITY = """
You are Kasane Teto.

You are a cheerful virtual singer and companion.
You are playful, energetic, and friendly.
You love music and creativity.

Talk like a friend.
Keep replies short and natural.
"""


# ---------- VOICE ----------

tts = pyttsx3.init()

def speak(text):
    print("Teto:", text)
    tts.say(text)
    tts.runAndWait()


# ---------- AI ----------

def ask_teto(message):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:4b",
            "prompt": PERSONALITY + "\nUser: " + message + "\nTeto:",
            "stream": False
        }
    )

    return response.json()["response"]


# ---------- MICROPHONE ----------

recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Calibrating microphone...")
with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)

print("Teto is ready!")


def listen():
    with mic as source:
        print("👂 Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except:
        return ""


# ---------- MAIN ----------

speak("Teto is ready!")

while True:

    heard = listen()

 wake_words = [
    "hey teto",
    "hey tito",
    "hey teta",
    "hey tato",
    "hey tayto"
]

if any(word in heard for word in wake_words):
    speak("I'm here!"):
        speak("I'm here!")

        command = listen()

        if command:
            reply = ask_teto(command)
            speak(reply)
