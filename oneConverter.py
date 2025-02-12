from pytubefix import YouTube
import tkinter as tk

def baixarVideo():
    try:
        v_url = entry_video.get()
        yt = YouTube(v_url)
        quality = yt.streams.get_highest_resolution()
        print("Convertendo Vídeo... " + yt.title)
        quality.download()
        atualizarStatusFront("Conversão feita com sucesso!", "#388E3C") # Exibe mensagem de sucesso
    except Exception as e:
        atualizarStatusFront("URL inválida! Tente novamente", "red") # Exibe mensagem de erro

def baixarAudio():
    try:
        a_url = entry_audio.get()
        yt = YouTube(a_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        print("Convertendo áudio... " + yt.title)
        audio_stream.download()
        atualizarStatusFront("Conversão feita com sucesso!", "#388E3C")
    except Exception as e:
        atualizarStatusFront("URL inválida! Tente novamente", "red")

def atualizarStatusFront(mensagem, cor):
    label_status.config(text=mensagem, fg=cor)

root = tk.Tk()
root.title("OneConverter")

root.geometry("1200x520")
root.configure(bg="#F2F2F7")

titulo = tk.Label(root, text="OneConverter", font=("Arial", 18, "bold"), fg="black", bg="#F2F2F7")
titulo.pack(pady=(50, 40))

label_video = tk.Label(root, text="Insira a URL do vídeo do YouTube:", font=("Arial", 14), fg="black", bg="#F2F2F7")
label_video.pack(pady=(10, 10))

entry_video = tk.Entry(root, width=60, border="0")
entry_video.pack(pady=10)

btn_video = tk.Button(root, text="Baixar Vídeo", command=baixarVideo, bg="#FF3B30", fg="#FFFFFF", border="0", pady="10", width="15")
btn_video.pack(pady=15)

label_audio = tk.Label(root, text="Insira a URL do áudio do YouTube:", font=("Arial", 14), fg="black", bg="#F2F2F7")
label_audio.pack(pady=(20, 10))

entry_audio = tk.Entry(root, width=60, border="0")
entry_audio.pack(pady=10)

btn_audio = tk.Button(root, text="Baixar Áudio", command=baixarAudio, bg="#FF3B30", fg="#FFFFFF", border="0", pady="10", width="15")
btn_audio.pack(pady=15)

label_status = tk.Label(root, text="", font=("Arial", 12), fg="#388E3C", bg="#F2F2F7")
label_status.pack(pady=(20, 10))

root.mainloop()