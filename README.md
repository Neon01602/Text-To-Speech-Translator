# Text-to-Speech Translator

## Overview

The **Text-to-Speech Translator** is a Python application that leverages speech recognition, translation, and text-to-speech technologies to convert spoken language into translated audio. Users can speak in their language, and the application will recognize the speech, translate it into a selected target language, and generate an audio file of the translation.

## Features

- **Speech Recognition**: Captures spoken input using the microphone.
- **Language Translation**: Translates recognized speech into various languages using the Google Translate API.
- **Text-to-Speech**: Converts translated text into audio using Google Text-to-Speech (gTTS).
- **Multi-language Support**: Supports a wide range of languages for translation.
- **Audio Playback**: Plays the generated audio file automatically.

## Supported Languages

The application supports the following languages for translation:

- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Chinese (Simplified) (zh-cn)
- Japanese (ja)
- Korean (ko)
- Russian (ru)
- Arabic (ar)
- Portuguese (pt)
- Hindi (hi)
- Bengali (bn)
- Turkish (tr)
- Vietnamese (vi)
- Tamil (ta)
- Telugu (te)
- Marathi (mr)
- Gujarati (gu)
- Malayalam (ml)
- Kannada (kn)
- Punjabi (pa)
- Urdu (ur)
- Assamese (as)

## Requirements

To run this application, you will need the following Python packages:

- `speech_recognition`
- `googletrans`
- `gtts`
- `playsound`

You can install these packages using pip:

```bash
pip install SpeechRecognition googletrans gTTS playsound
