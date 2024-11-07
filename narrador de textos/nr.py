from gtts import gTTS
import os

# Texto que você quer narrar
text = "Sou Joã0"

# Cria o objeto gTTS
tts = gTTS(text=text, lang='pt')

# Salva o áudio em um arquivo
tts.save("narracao.mp3")

# Reproduz o áudio
os.system("narracao.mp3")
