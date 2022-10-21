import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
	print('Diga algo familia')
	audio = recon.listen(source)

print(recon.recognize_google(audio, language = 'pt'))