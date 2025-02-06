from pytubefix import YouTube

print("ConverteAI")

def baixarVideo ():
    v_url = input("Você quer fazer o download de um vídeo do Youtube? Insira a URL aqui:")

    yt = YouTube(v_url)

    quality = yt.streams.get_highest_resolution()
    print("Convertendo Vídeo... " + yt.title)
    quality.download()

    print("Conversão feita com sucesso :)")

def baixarAudio():
    a_url = input("Você quer extrair o áudio de um vídeo do Youtube, e fazer download? Insira a URL aqui: ")

    yt = YouTube(a_url)
    
    audio_stream = yt.streams.filter(only_audio=True).first()
    print("Convertendo áudio... " + yt.title)
    audio_stream.download()
    
    print("Conversão feita com sucesso :)")

baixarAudio()

