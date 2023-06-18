# ****** For downloading videos ****** #

from pytube import YouTube

link = "YOUR_YOUTUBE_VIDEO_LINK"
youtube1 = YouTube(link)

videos = youtube1.streams
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
stm = int(input("Enter the quality index: "))
videos[stm].download()
print("Successfully downloaded!!")

# ****** For downloading playlist ****** #

from pytube import Playlist

py = Playlist("")  #Give the playlist link here

print(f"Downloading {py.title}")

for video in py.videos:
    video.streams.first().download()
