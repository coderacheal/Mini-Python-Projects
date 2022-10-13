#pip install pyttsx3
import pyttsx3

text_to_speech = pyttsx3.init()
print(type(text_to_speech))
my_text = input('Enter your text: ')

text_to_speech.say(my_text)
text_to_speech.runAndWait()