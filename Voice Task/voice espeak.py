import subprocess


def text_to_speech_save_wav(text, output_filename, voice_variant="en+f3", speed=145, pitch=65):
    """
    Convert text to speech using eSpeak and save as WAV file

    Parameters:
        text (str): Text to convert to speech
        output_filename (str): Output WAV file path
        voice_variant (str): Voice variant (default: "f3" - female voice)
        speed (int): Speech speed in words per minute (default: 150)
        pitch (int): Pitch adjustment (0-99, default: 60)
    """
    # Construct the eSpeak command
    command = [
        r"C:\Program Files (x86)\eSpeak\command_line\espeak.exe",  # Path to espeak.exe
        "-v", voice_variant,  # Voice variant
        "-s", str(speed),  # Speed adjustment
        "-p", str(pitch),  # Pitch adjustment
        "-a", "150",  # Amplitude (volume)
        "-g", "10",  # Word gap (pause between words)
        "-w", output_filename,  # Output WAV file
        text  # Text to speak
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Speech saved as '{output_filename}'")
        print(f"Settings used: Voice={voice_variant}, Speed={speed}, Pitch={pitch}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating speech: {e}")
    except FileNotFoundError:
        print("Error: eSpeak not found. Please ensure eSpeak is installed at the specified path.")


# The message to convert
message = "You're not just a friend, you're family. I'm so grateful for our bond and the memories we've shared. Here's to many more adventures together!"

# Generate the speech with different settings
text_to_speech_save_wav(
    text=message,
    output_filename="friendship_message.wav",
    voice_variant="en+f3",  # Female voice (try "f1", "f2", "f3", "f4", "f5")
    speed=145,  # Slightly slower for more natural delivery
    pitch=65  # Slightly higher pitch for warmth
)

print("\nTip: For better quality, try these voice variants:")
print("- 'en-us+f3' for American English female voice")
print("- 'en+f4' for British English female voice")
print("- 'mb-en1' for more natural male voice")
print("Adjust speed (120-160) and pitch (50-70) for different effects")