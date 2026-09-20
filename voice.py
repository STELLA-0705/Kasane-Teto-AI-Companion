import pyttsx3
import config

engine = pyttsx3.init("sapi5")

engine.setProperty("rate", config.VOICE_RATE)


def speak(text):

    print()

    print("🎤 Teto:", text)

    engine.say(str(text))

    engine.runAndWait()