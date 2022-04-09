from pytube import YouTube

class YoutubeDownloader:
	def __init__(self, link):
		self.link = link

	def video_name(self):
		video = YouTube(self.link)	
		return video.title

	def audio_downloader(self):
		try:
			video = YouTube(self.link)	
			stream = video.streams.get_audio_only()
			stream.download("Downloads/", filename=f"{video.title}.mp3")
			return True
			
		except:
			return False

	def video_downloader(self):
		try:
			video = YouTube(self.link)	
			stream = video.streams.get_highest_resolution()
			stream.download("Downloads/")
			return True
		
		except:
			return False