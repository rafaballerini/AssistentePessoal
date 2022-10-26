# Assistente Pessoal com Python

Fala pessoal, essa é a Ana, uma assistente pessoal virtual que escuta os seus comandos de voz e executa-os!

### Features:
* ⌚ Que horas são
* 🔎 Pesquisa no Google
* 🪙 Cotação de dólar, euro e bitcoin
* 📰 Últimas 5 notícias do momento
* 📽️ 5 filmes mais populares do momento
* 🎧 Abrir a melhor música, banda e álbum do mundo no Spotify
* 💤 Desligar computador em 1 hora ou meia hora
* ❌ Cancelar desligamento do computador
* 🙋🏽‍♀️ Fechar a assistente

### Tecnologias utilizadas:

* [Python](https://www.python.org/): linguagem de programação
* [Speech Recognition](https://pypi.org/project/SpeechRecognition/): reconhecimento de voz
* [gTTS](https://pypi.org/project/gTTS/): sintetização de voz
* [Playsound](https://pypi.org/project/playsound/): executador de áudio
* [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/): para leitura de páginas elementos em páginas web
* Outras: os, sys, webbrowser, urllib.request, json, datetime, requests

### Como executar:

**1. Instale `Python` na sua máquina, por meio [deste link](https://www.python.org/)**

**2. Faça um clone [desse repositório](https://github.com/rafaballerini/AssistentePessoal.git) na sua máquina:**

* Crie uma pasta no seu computador para esse programa, recomendo colocar o nome **Assistente Pessoal**
* Abra o `git bash` ou `terminal` dentro dessa pasta
* Copie a [URL](https://github.com/rafaballerini/AssistentePessoal.git) do repositório
* Digite `git clone <URL copiada>` e pressione `enter`

**3. Instale as bibliotecas necessárias pelo terminal, dentro dessa pasta criada:**

* gTTS: `pip install gTTS`
* playsound: `pip install playsound`
* beautiful soup 4: `pip install beautifulsoup4`
* speech recognition: `pip install SpeechRecognition`
caso apareça algum erro referente a alguma das bibliotecas importadas no programa, jogue o nome dela no Google e faça a instalação e passo a passo necessários

**4. Crie sua chave para a API de filmes:**
* Acesse o [The Movie DataBase](https://www.themoviedb.org/) e faça seu cadastro
* Em configurações, acesse API e crie uma nova chave
* Copie a chave e cole na URL da linha 54 do código, substituindo a frase `<suachaveapi>`

**5. Execute o programa pelo terminal:**
* Digite `python assistente.py`

### Estudos:

Na pasta `estudos` você escontra alguns códigos simples, que eu utilizei para aprender sobre as ferramentas, inclusive utilizando outras como [espeak](https://espeak.sourceforge.net/) e [pyttsx3](https://pypi.org/project/pyttsx3/)
