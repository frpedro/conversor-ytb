from pytubefix import YouTube
import tkinter as tk

def baixar_video():
    try:
        v_url = entry_video.get()  # Pega URL
        yt = YouTube(v_url)
        qualidade = yt.streams.get_highest_resolution()  # Busca automaticamente a melhor qualidade disponível.
        print("Convertendo Vídeo... " + yt.title)
        qualidade.download()  # Realiza o download.
        atualizar_status_front("Conversão feita com sucesso!", "#388E3C")
    except Exception as e:
        atualizar_status_front("URL inválida! Tente novamente", "red")

def baixar_audio():
    try:
        a_url = entry_audio.get()
        yt = YouTube(a_url)
        audio_stream = yt.streams.filter(only_audio=True).first()  # Configura a busca apenas de áudio.
        print("Convertendo áudio... " + yt.title)
        audio_stream.download()  # Realiza o download.
        atualizar_status_front("Conversão feita com sucesso!", "#388E3C")
    except Exception as e:
        atualizar_status_front("URL inválida! Tente novamente", "red")

# Função de atualização do status da conversão na interface.
def atualizar_status_front(mensagem, cor):
    label_status.config(text=mensagem, fg=cor)

# Inicia a interface.
root = tk.Tk()
root.title("OneConverter")

# Ajusta tamanho e background da janela.
root.geometry("1200x520")
root.configure(bg="#F2F2F7")

# Título.
titulo = tk.Label(root, text="OneConverter", font=("Arial", 18, "bold"), fg="black", bg="#F2F2F7")
titulo.pack(pady=(50, 40))

# Label para download de vídeo.
label_video = tk.Label(root, text="Insira a URL do vídeo do YouTube:", font=("Arial", 14), fg="black", bg="#F2F2F7")
label_video.pack(pady=(10, 10))

# Entrada para URL do vídeo.
entry_video = tk.Entry(root, width=60, border="0")
entry_video.pack(pady=10)

# Botão para baixar vídeo.
btn_video = tk.Button(root, text="Baixar Vídeo", command=baixar_video, bg="#FF3B30", fg="#FFFFFF", border="0", pady="10", width="15")
btn_video.pack(pady=15)

# Label para download de áudio.
label_audio = tk.Label(root, text="Insira a URL do áudio do YouTube:", font=("Arial", 14), fg="black", bg="#F2F2F7")
label_audio.pack(pady=(20, 10))

# Entrada para URL do áudio
entry_audio = tk.Entry(root, width=60, border="0")
entry_audio.pack(pady=10)

# Botão para baixar áudio
btn_audio = tk.Button(root, text="Baixar Áudio", command=baixar_audio, bg="#FF3B30", fg="#FFFFFF", border="0", pady="10", width="15")
btn_audio.pack(pady=15)

# Atualiza o status da conversão na interface.
label_status = tk.Label(root, text="", font=("Arial", 12), fg="#388E3C", bg="#F2F2F7")
label_status.pack(pady=(20, 10))

# Roda a interface
root.mainloop()
