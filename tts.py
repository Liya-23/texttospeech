import os
from gtts import gTTS
import shutil

# Get user input
text = input("Enter some text: ")
#firsr read file 
#readtheFile = open("module5demo.txt", "rt")
#save the file in a string format
ourFileInText = str(text)
#call the string format on txt

# f1 = open(module5sec1.txt)
# Set language and generate audio file
language = 'en'
tts = gTTS(text=ourFileInText, lang=language)

# Save audio file
filename = input("save file as? ")
tts.save(filename + ".mp3")
#formatee = 
#saving to a different directory
shutil.move("audio.mp3", "audios/file_name.mp3")
# Play audio file
os.system(filename)
