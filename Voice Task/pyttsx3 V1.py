import pyttsx3


def tts_pyttsx3(text, output_file, voice_id=None):
    engine = pyttsx3.init()

    # Set properties for better quality
    engine.setProperty('rate', 150)  # Speed (words per minute)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Get available voices
    voices = engine.getProperty('voices')

    if voice_id:
        engine.setProperty('voice', voice_id)
    else:
        # Try to select a female voice
        for voice in voices:
            if "female" in voice.name.lower() or "zira" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

    # Save to file
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    print(f"✅ Saved voice to '{output_file}'")


# Usage
text = "Welcome  to Our ChatBot . How Can i help You . feel free to ask Question to me ?"
tts_pyttsx3(text, "pyttsx3_output.wav")
