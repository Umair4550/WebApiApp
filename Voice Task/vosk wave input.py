import wave
import json
from vosk import Model, KaldiRecognizer

# Load your Vosk model directory
model_path = r"C:\Users\hp\Downloads\vosk-model-en-us-0.22\vosk-model-en-us-0.22"
model = Model(model_path)

# Path to your audio file
audio_path = r"C:\Users\hp\FYP Python Work\ChatBot Api\Voice Task\pyttsx3_output.wav"

# Open audio file
wf = wave.open(audio_path, "rb")

# Make sure audio is mono and 16kHz
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
    print("❌ Please ensure the WAV file is mono (1 channel), 16-bit, 16kHz.")
    exit()

# Initialize recognizer
rec = KaldiRecognizer(model, wf.getframerate())

# Transcribe
results = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        results.append(result.get("text", ""))
    else:
        pass  # skip partials if not needed

# Final result
final_result = json.loads(rec.FinalResult())
results.append(final_result.get("text", ""))

# Print full transcription
full_text = " ".join(results)
print("📝 Transcription:\n", full_text)
