from moviepy.editor import VideoFileClip
from re import search

class VideoConverter:
    def __init__(self, caminho):
        self.caminho = caminho

    def __audioName(self):
        pattern = r"([0-9a-zA-Z_\-@ ])+\."

        try:
            match = search(pattern, self.caminho)
            audioName = f"{match.group()}mp3"
            return audioName

        except AttributeError:
            audioName = "audio.mp3"
            return audioName

    def converter(self):
        try:
            videoclip = VideoFileClip(self.caminho)

            audioclip = videoclip.audio
            audioclip.write_audiofile(self.__audioName())

            audioclip.close()
            videoclip.close()

        except OSError:
            print("\n" + " " * 6 + "Erro")
            print("-" * 17)
            print("Caminho Inválido!")
            print("-" * 17)