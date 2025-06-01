import subprocess

def text_to_speech_cmd_style(text, output_filename):
    # Properly formatted text with quotes for CMD
    formatted_text = f'"{text}"'

    command = (
        f'"C:\\Program Files (x86)\\eSpeak\\command_line\\espeak.exe" '
        f'-s 155 '
        f'-w "{output_filename}" {formatted_text}'
    )

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ Speech saved to: {output_filename}")
    except subprocess.CalledProcessError as e:
        print("❌ Error generating speech:", e)
    except FileNotFoundError:
        print("❌ eSpeak not found at the given path.")


# Usage
message = (
    "i Fuck you  fuck you ass . Your Ass is so Big and Very beautiful .Come Onn Baby Aa na  "

)

text_to_speech_cmd_style(message, "friendship_message.wav")
