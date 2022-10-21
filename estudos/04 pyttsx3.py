# Usando um arquivo de texto a ser lido e falado
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

arquivo = open("frase.txt", "r", encoding = "utf-8")
conteudo = arquivo.read()
engine.say(conteudo)
print(conteudo)
arquivo.close()
engine.runAndWait()