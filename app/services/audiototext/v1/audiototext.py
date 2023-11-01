"""
Speech Recognition System
"""
import base64
from io import BytesIO
import speech_recognition as sr
from pydub import AudioSegment


class Audiototext:
    """Audio To Text"""
    def __init__(self, input_data) -> None:
        self.base64_audio = input_data.get('text', None)

    def post(self):
        """Post"""
        try:
            # Decode the base64 data
            audio_bytes = base64.b64decode(self.base64_audio['data'])

            # Convert the bytes to an AudioSegment
            audio = AudioSegment.from_file(BytesIO(audio_bytes))

            # Save the audio as a temporary WAV file
            audio.export("temp_audio.wav", format="wav")

            # Initialize the recognizer
            recognizer = sr.Recognizer()

            # Recognize speech from the audio file
            with sr.AudioFile("temp_audio.wav") as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
            return text
        except Exception as e:
            print("An error occurred while transcribing the audio:", str(e))
            return None
