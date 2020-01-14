import pytube

url = "https://www.youtube.com/watch?v=EPe0BOJDMcA"

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download(r'C:\Users\lazar\Desktop)
