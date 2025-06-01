import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# Load your Vosk model directory
model_path = r"C:\Users\hp\Downloads\vosk-model-en-us-0.22\vosk-model-en-us-0.22"
model = Model(model_path)

# Audio input settings
samplerate = 16000  # 16 kHz sample rate
q = queue.Queue()

# Initialize recognizer
rec = KaldiRecognizer(model, samplerate)

# Callback to feed audio into queue
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# Start audio stream
with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("🎙️ Speak into the microphone... (Press Ctrl+C to stop)")

    try:
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                print("📝", result.get("text", ""))
            else:
                partial = json.loads(rec.PartialResult())
                # Optionally show partial results:
                # print("...", partial.get("partial", ""))
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
