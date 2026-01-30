#pip install pytsx3
import pyttsx3
engine = pyttsx3.init()


engine.say("I will speak this text because you have used a text to speech module of python.")
engine.runAndWait()