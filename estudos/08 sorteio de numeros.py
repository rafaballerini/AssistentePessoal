# Tentando acertar um numero aleatorio
from random import randint
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound

def cria_audio(audio, mensagem):
	tts = gTTS(mensagem, lang = 'pt-br')
	tts.save(audio)
	playsound(audio)

cria_audio('intro.mp3', "Olá, sou a Ana! Escolha um número entre 1 e 10")	

recon = sr.Recognizer()

with sr.Microphone() as source:
	print('Estou ouvindo, pode falar')
	audio = recon.listen(source)

numero = (recon.recognize_google(audio, language = 'pt'))

resultado = randint(1, 10)

if numero == resultado:
	cria_audio('venceu.mp3', "parabens, você acertou o número")
else:
	cria_audio('errou.mp3', "voce errou")