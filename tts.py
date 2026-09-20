import pyttsx3

# Start Windows TTS
engine = pyttsx3.init()

# Change this text later to your AI response
text = "Hello! I am your virtual companion. Nice to meet you!"

engine.say(text)

# Speak it
engine.runAndWait()