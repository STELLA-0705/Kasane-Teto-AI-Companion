# Teto_Companion.py

import speech
import wakeword
import Teto_Brain as brain
import voice
import time


print("✨ Teto AI Companion started!")
print("💤 Waiting for 'Hey Teto'...")


def main():

    while True:

        try:
            heard = speech.listen()

            if not heard:
                continue


            print("Heard:", heard)


            if wakeword.is_teto(heard):

                print("✨ Wake word detected!")

                voice.speak(
                    "I'm here!"
                )


                question = speech.listen()


                if question:

                    print("🧠 Teto is thinking...")

                    answer = brain.ask(
                        question
                    )


                    print(
                        "AI RESPONSE:",
                        answer
                    )


                    voice.speak(
                        answer
                    )


                print("💤 Waiting for 'Hey Teto'...")


        except KeyboardInterrupt:

            print("\n👋 Teto shutting down.")

            break


        except Exception as e:

            print(
                "⚠️ Error:",
                e
            )

            time.sleep(1)



if __name__ == "__main__":
    main()