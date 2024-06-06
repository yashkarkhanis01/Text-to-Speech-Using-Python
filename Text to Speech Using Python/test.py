from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Play the audio

def main():
    print("Welcome to Text-to-Speech Converter!")
    text = input("Enter the text you want to convert to speech: ")
    language = input("Enter the language (optional, press Enter for default 'en'): ")
    
    if language:
        text_to_speech(text, language)
    else:
        text_to_speech(text)

    print("Audio generated and played. Thank you!")

if __name__ == "__main__":
    main()
