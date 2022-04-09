from tkinter import Label, Tk, Button, Entry
from tkinter.ttk import Progressbar
from Classes.YoutubeDownloader import YoutubeDownloader
from Classes.VideoConverter import VideoConverter
from time import sleep

# Frame
root = Tk()
root.title("Maravipenis")
root.resizable(width=False, height=False)
root.configure(bg="gray")

# Funções

def barra_progresso():
    progresso.start()

def audio_downloader():
    audio = YoutubeDownloader(linkEntry.get())

    if audio.audio_downloader():
        status["text"] = f"Audio: {audio.video_name()}"

def video_downloader():
    video = YoutubeDownloader(linkEntry.get())

    if video.video_downloader():
        status["text"] = f"Video: {video.video_name()}"

def video_converter():
    caminho = VideoConverter(linkEntry.get())
    caminho.converter()

# Barra de Progresso
progresso = Progressbar(root, length=10, orient="horizontal",mode="indeterminate")

# Legendas
linkLeg = Label(root, text="Caminho:", font="Times 15 italic")
status = Label(root, font="Times 12 italic", pady=10, relief="ridge")

# Caixa de entrada
linkEntry = Entry(root, width=50, insertbackground="gray", font="Times 12 italic")

# Botão
audio = Button(root, text="Audio", width=15, command=audio_downloader)
video = Button(root, text="Video", width=15, command=video_downloader)
videoConverter = Button(root, text="Video to Mp3", command=video_converter)

# Packing
linkLeg.grid(row=0, columnspan=2, sticky="ew") # Lbl 
status.grid(row=3, columnspan=2, sticky="ew") # Lbl

linkEntry.grid(row=1, columnspan=2, sticky="ew") # Entry
linkEntry.focus()

progresso.grid(row=2, columnspan=2, sticky="ew", pady=2) # Bar

video.grid(row=4,column=0, sticky="we") # Btn
audio.grid(row=4,column=1, sticky="ew") # Btn
videoConverter.grid(row=5, columnspan=2, sticky="ew") # Btn

print(progresso.start)
root.mainloop()