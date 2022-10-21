import os
import sys
import re, unicodedata, requests, bs4 
import speech_recognition as sr 
import webbrowser as browser
import urllib.request, json
from unicodedata import normalize
from gtts import gTTS
from playsound import playsound
from datetime import datetime
from bs4 import BeautifulSoup
from requests import get

def cria_audio(audio, mensagem, lang = 'pt-br'):
	tts = gTTS(mensagem, lang = lang)
	tts.save(audio)
	playsound(audio)
	os.remove(audio)	

def monitora_audio():
	recon = sr.Recognizer()
	with sr.Microphone() as source:
		while True:
			print('Diga algo, estou te ouvindo')
			audio = recon.listen(source)
			try: 
				mensagem = recon.recognize_google(audio, language = 'pt-br')
				mensagem = mensagem.lower()
				print('Você disse', mensagem)
				executa_comandos(mensagem)
				break
			except sr.UnknownValueError:
				pass
			except sr.RequestError:
				pass
		return mensagem

def noticias():
	site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
	noticias = BeautifulSoup(site.text, 'html.parser')
	for item in noticias.findAll('item')[:5]:
		mensagem = item.title.text
		cria_audio('audios/noticias.mp3', mensagem)

def cotacao(moeda):
	requisicao = get(f'https://economia.awesomeapi.com.br/all/{moeda}-BRL')
	cotacao = requisicao.json()
	nome = cotacao[moeda]['name']
	data = cotacao[moeda]['create_date']
	valor = cotacao[moeda]['bid']
	cria_audio("audios/cotacao.mp3", f"Cotação do {nome} em {data} é {valor}")

def filmes():
	url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=337ed39273b212f686420bb756fee987'
	resposta = urllib.request.urlopen(url)
	dados = resposta.read()
	jsondata = json.loads(dados)
	filmes = jsondata['results']
	for filme in filmes[:5]:
		cria_audio("audios/filmes.mp3", filme['title'], lang = 'en')

'''
def previsao():
	url = "http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=fa65a2a9cde8f5d447c48c8f4a0f6848"
	resposta = urllib.request.urlopen(url)
	dados = resposta.read()
	jsondata = json.loads(dados)
	#previsao = jsondata['']
	print(jsondata)
'''

def executa_comandos(mensagem):

	# fechar assistente
	if 'fechar assistente' in mensagem:
		sys.exit()

	# hora atual
	elif 'horas' in mensagem:
		hora = datetime.now().strftime('%H:%M')
		frase = f"Agora são {hora}"
		cria_audio('audios/horas.mp3', frase)

	# desligar o computador
	elif 'desligar computador' in mensagem and 'uma hora' in mensagem:
		os.system("shutdown -s -t 3600")
	elif 'desligar computador' in mensagem and 'meia hora' in mensagem:
		os.system("shutdown -s -t 1800")
	elif 'cancelar desligamento' in mensagem:
		os.system("shutdown -a")

	# pesquisa no google
	elif 'pesquisar' in mensagem:
		mensagem = mensagem.replace('pesquisar', '')
		browser.open(f'https://google.com/search?q={mensagem}')

	# spotify
	elif 'melhor' in mensagem and 'música' in mensagem:
		browser.open('https://open.spotify.com/track/2jvuMDqBK04WvCYYz5qjvG?si=d5118879d68540f3')
	elif 'melhor' in mensagem and 'banda' in mensagem:
		browser.open('https://open.spotify.com/playlist/37i9dQZF1DZ06evO07zaak?si=2cc1a14c1146467a')
	elif 'melhor' in mensagem and 'álbum' in mensagem:
		browser.open('https://open.spotify.com/album/4LH4d3cOWNNsVw41Gqt2kv?si=9f6e7d7bcb474666')
	elif 'playlist' in mensagem and 'rock' in mensagem:
		browser.open('https://open.spotify.com/playlist/5TUxgTIxzLbLVh7RUf9V8i?si=4567c0415d0647b1')
	elif 'playlist' in mensagem and 'eletronica' in mensagem:
		browser.open('https://open.spotify.com/playlist/2HszJWnlslyuye9GFZQJQc?si=81537070a51d4c97')
	elif 'playlist' in mensagem and 'brasileira' in mensagem:
		browser.open('https://open.spotify.com/playlist/7ngeDvP8gp3ZtCGfq68jUV?si=49e62791666242a8')

	# notícias
	elif 'notícias' in mensagem:
		noticias()

	# cotação de moedas
	elif 'dólar' in mensagem:
		cotacao('USD')
	elif 'euro' in mensagem:
		cotacao('EUR')
	elif 'bitcoin' in mensagem:
		cotacao('BTC')

	# filmes
	elif 'filmes' in mensagem and 'populares' in mensagem:
		filmes()

'''
	# previsão do tempo
	elif 'previsão' in mensagem:
		previsao()
'''

def main():
	cria_audio("audios/ola.mp3", "Olá sou a Ana, sua assistente virtual! Como posso ajudar?")
	while True:
		monitora_audio()

main()