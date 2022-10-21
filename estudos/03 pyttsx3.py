# Digitar frase a ser falada no terminal
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
frase = input("Digite a frase a ser falada:\n")
engine.say(frase)
engine.runAndWait()