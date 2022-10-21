import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound

def cria_audio(audio, mensagem):
	tts = gTTS(mensagem, lang = 'pt-br')
	tts.save(audio)
	playsound(audio)

cria_audio("welcome.mp3", "Olá, sou a Ana! Vou reconhecer a sua voz.")	

recon = sr.Recognizer()

with sr.Microphone() as source:
	print('Diga algo')
	audio = recon.listen(source)

frase = (recon.recognize_google(audio, language = 'pt'))
cria_audio("mensagem.mp3", frase)