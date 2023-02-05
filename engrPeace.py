import speech_recognition as sr
import random
import time


print(sr.__version__)
# this prints the module version

D = sr.Recognizer()
M = sr.Microphone()
harvard = sr.AudioFile('audio_files_harvard.wav')
jack = sr.AudioFile('audio_files_jackhammer.wav')
fox = sr.AudioFile('fox.wav')

with harvard as source:
    audio = D.record(source, offset=5, duration=7)

with jack as source:
    D.adjust_for_ambient_noise(source)
    audio1 = D.record(source)

with fox as source:
    # this says "the quick brown fox jumps over the lazy dog"
    D.adjust_for_ambient_noise(source)
    audio2 = D.record(source)

# this allows the recording of audio
# with M as source:
#     print("recording")
#     voice = D.listen(source)
#     print("done")


D.recognize_google(audio2)
