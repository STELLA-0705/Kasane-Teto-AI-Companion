import speech

print("🎤 Say something!")

while True:
    text = speech.listen()

    if text:
        print("RESULT:", text)