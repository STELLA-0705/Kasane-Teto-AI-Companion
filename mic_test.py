import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

print("Starting mic test...")

with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)

print("Say: hello teto")

with mic as source:
    audio = recognizer.listen(source)

print("Audio captured!")

try:
    text = recognizer.recognize_google(audio)
    print("I heard:", text)

except Exception as e:
    print("Error:", e)