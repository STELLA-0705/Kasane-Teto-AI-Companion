import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

def listen_to_user():

    with mic as source:
        print("🎤 Teto is listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        print("You:", text)
        return text

    except sr.UnknownValueError:
        print("Couldn't understand.")
        return ""

    except sr.RequestError:
        print("Speech service error.")
        return ""


while True:
    message = listen_to_user()

    if message:
        print("Teto heard:", message)