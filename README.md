# Text-to-Speech Translator

## Description

The Text-to-Speech Translator is a Python application that leverages advanced machine learning models and natural language processing techniques to recognize hand gestures representing letters and translate them into spoken language. This application is designed for educational purposes and aims to assist individuals in learning sign language by providing real-time translations of hand gestures into various spoken languages.

## Features

- **Hand Gesture Recognition**: Utilizes computer vision to detect hand gestures and recognize corresponding letters.
- **Multi-Language Support**: Translates recognized letters into multiple languages, including but not limited to Spanish, French, German, Chinese, and more.
- **Text-to-Speech Conversion**: Converts translated text into speech using Google Text-to-Speech (gTTS).
- **User -Friendly Interface**: Built with Tkinter for a simple and intuitive user experience.
- **Snapshot Functionality**: Allows users to take snapshots of recognized gestures and save them for future reference.

## Requirements

To run this project, you will need the following libraries:

- Python 3.x
- OpenCV
- Mediapipe
- TensorFlow
- NumPy
- gTTS
- SpeechRecognition
- Googletrans
- Pillow
- Tkinter

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe tensorflow numpy gtts SpeechRecognition googletrans==4.0.0-rc1 Pillow
