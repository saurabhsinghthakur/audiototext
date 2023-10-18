"""
Speech Recognition System
"""
from pydantic import BaseModel
import speech_recognition as sr
import numpy as np

class AudioFile(BaseModel):
    """Audio File Validator"""
    path: str

class Audiototext:
    """Audio File Processor"""
    def __init__(self, audio_file) -> None:
        self.audio_file = audio_file

    def post(self):
        """Recognize large audio"""
        recognizer = sr.Recognizer()

        # Read the entire audio file
        with sr.AudioFile(self.audio_file.file) as source:
            audio_data = recognizer.record(source)

        audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)

        # Get the duration of the audio file in seconds
        total_duration = len(audio_array) / audio_data.sample_rate

        chunk_size = 10  # Set your desired chunk size in seconds
        start_time = 0

        recognized_text = ""
        while start_time < total_duration:
            end_time = min(start_time + chunk_size, total_duration)
            start_index = int(start_time * audio_data.sample_rate)
            end_index = int(end_time * audio_data.sample_rate)
            chunk = audio_array[start_index:end_index].tobytes()

            try:
                chunk_audio_data = sr.AudioData(chunk, audio_data.sample_rate, audio_data.sample_width)
                chunk_text = recognizer.recognize_google(chunk_audio_data, show_all=False)
                recognized_text += " " + chunk_text
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

            start_time += chunk_size

        return recognized_text.strip()
