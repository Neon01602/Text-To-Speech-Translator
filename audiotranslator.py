import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import subprocess
from playsound import playsound

languages = {
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Chinese (Simplified)': 'zh-cn',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Arabic': 'ar',
    'Portuguese': 'pt',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Turkish': 'tr',
    'Vietnamese': 'vi',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Malayalam': 'ml',
    'Kannada': 'kn',
    'Punjabi': 'pa',
    'Urdu': 'ur',
    'Assamese': 'as',
}

def display_languages():
    print("Available languages for translation:")
    print("Available languages and their codes: "
      "Spanish: es, "
      "French: fr, "
      "German: de, "
      "Italian: it, "
      "Chinese (Simplified): zh-cn, "
      "Japanese: ja, "
      "Korean: ko, "
      "Russian: ru, "
      "Arabic: ar, "
      "Portuguese: pt, "
      "Hindi: hi, "
      "Bengali: bn, "
      "Turkish: tr, "
      "Vietnamese: vi, "
      "Tamil: ta, "
      "Telugu: te, "
      "Marathi: mr, "
      "Gujarati: gu, "
      "Malayalam: ml, "
      "Kannada: kn, "
      "Punjabi: pa, "
      "Urdu: ur, "
      "Assamese: as")

def main():

    recognizer = sr.Recognizer()
    translator = Translator()
    choice = input("Want to continue?")
    while choice.lower() != "no":
        with sr.Microphone() as source:
            print("Please speak something...")
            audio = recognizer.listen(source)

        try:
        
            recognized_text = recognizer.recognize_google(audio)
            print(f"You said: {recognized_text}")

            display_languages()
            target_language_name = input("Enter the name of the target language: ")

            target_language = languages.get(target_language_name)
            if not target_language:
                print("Sorry, that language is not available.")
                return

            translated_text = translator.translate(recognized_text, dest=target_language).text
            print(f"Translated text: {translated_text}")
            
            tts = gTTS(text=translated_text, lang=target_language)
            audio_file = "translated_audio.mp3"
            tts.save(audio_file)
            print(f"Audio file saved as {audio_file}")
            if os.path.exists(audio_file):
                print("Playing audio...")
                # Play the generated audio using subprocess
                subprocess.run(["start", audio_file], shell=True)  # For Windows
            else:
                print("Audio file was not created.")

            
            
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        

if __name__ == "__main__":
        main()