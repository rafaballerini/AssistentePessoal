# Criando audio a partir de arquivo txt e executando
from gtts import gTTS
from playsound import playsound

def cria_audio(mensagem):
	tts = gTTS(mensagem, lang = 'pt-br')
	tts.save('hello.mp3')
	playsound('hello.mp3')

arquivo = open("frase.txt", "r", encoding = "utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)
arquivo.close()