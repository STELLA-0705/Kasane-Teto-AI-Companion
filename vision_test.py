import time
import vision


print("Teto's eyes are open 👀")

while True:

    if vision.see():
        print("👀 Teto sees you!")

    else:
        print("💤 No one detected")

    time.sleep(2)