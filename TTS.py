# Here is my lovely Text To Speech project in under 10 lines of code!

from gtts import gTTS
import os

# "sample.txt" was the text file I sampled, any text file will work.
f = open("sample.txt")
x = f.read()

# Customize the Language accordingly.
language = 'en'

audio = gTTS(text=x, slow=False)

# This will work for Windows or even Linux users.
audio.save("audio.wav")
os.system("audio.wav")
