from pytubefix import YouTube #classe da lib pytubefix
import tkinter as tk #lib de interface

def baixarVideo():
    v_url = entry_video.get()
    yt = YouTube(v_url)
    quality = yt.streams.get_highest_resolution() # Busca automáticamente a melhor qualidade disponível.
    print("Convertendo Vídeo... " + yt.title)
    quality.download() # Realiza o download.
    print("Conversão feita com sucesso :)")

def baixarAudio():
    a_url = entry_audio.get()
    yt = YouTube(a_url)
    audio_stream = yt.streams.filter(only_audio=True).first() #Configura a busca apenas de áudio.
    print("Convertendo áudio... " + yt.title)
    audio_stream.download() # Realiza o download.
    print("Conversão feita com sucesso :)")

# Inicia a interface.
root = tk.Tk()
root.title("OneConverter")

# Ajusta tamanho da janela.
root.geometry("1200x500")

# Configura background da janela.
root.configure(bg="#F2F2F7")

# Título.
titulo = tk.Label(root, text="OneConverter", font=("Arial", 18, "bold"), fg="black", bg="#F2F2F7")
titulo.pack(pady=(50, 40)) 

# Label para download de vídeo.
label_video = tk.Label(root, text="Insira a URL do vídeo do YouTube:", font=("Arial", 14), fg="black", bg="#F2F2F7")
label_video.pack(pady=(10, 10))  # Ajuste na margem superior

# Entrada para URL do vídeo.
entry_video = tk.Entry(root, width=60, border="0")
entry_video.pack(pady=10)

# Botão para baixar vídeo.
btn_video = tk.Button(root, text="Baixar Vídeo", command=baixarVideo, bg="#FF3B30", fg="#FFFFFF", border="0",  pady="10", width="15")
btn_video.pack(pady=15)

# Label para download de áudio.
label_audio = tk.Label(root, text="Insira a URL do áudio do YouTube:", font=("Arial", 14), fg="black", bg="#F2F2F7")
label_audio.pack(pady=(20, 10))

# Entrada para URL do áudio
entry_audio = tk.Entry(root, width=60, border="0")
entry_audio.pack(pady=10)

# Botão para baixar áudio
btn_audio = tk.Button(root, text="Baixar Áudio", command=baixarAudio, bg="#FF3B30", fg="#FFFFFF", border="0", pady="10", width="15")
btn_audio.pack(pady=15)

# Roda a interface
root.mainloop()
