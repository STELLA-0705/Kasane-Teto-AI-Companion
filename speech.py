import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel
import tempfile
import os


# Your Samson mic
MIC_DEVICE = 1

SAMPLE_RATE = 16000
RECORD_SECONDS = 5


print("Loading Whisper...")
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper ready!")


def record_audio():

    print("🎤 Listening...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=MIC_DEVICE
    )

    sd.wait()

    return audio


def listen():

    audio = record_audio()

    filename = "teto_input.wav"

    sf.write(
        filename,
        audio,
        SAMPLE_RATE
    )


    print("🧠 Thinking about words...")


    segments, info = model.transcribe(
        filename,
        beam_size=1,
	language="en"
    )


    text = ""

    for segment in segments:
        text += segment.text


    text = text.strip().lower()


    if text:
        print("You:", text)

    else:
        print("❌ Nothing heard")


    return text