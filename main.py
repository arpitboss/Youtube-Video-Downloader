# ****** For downloading videos ****** #

from pytube import YouTube

link = "https://www.youtube.com/watch?v=Glmv0wj4xpo"
youtube1 = YouTube(link)

# print(youtube1.title)
# print(youtube1.thumbnail_url)

videos = youtube1.streams
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
stm = int(input("Enter the quality index: "))
videos[stm].download()
print("Successfully downloaded!!")

# ****** For downloading playlist ****** #

# from pytube import Playlist
#
# py = Playlist("")  #Give the playlist link here
#
# print(f"Downloading {py.title}")
#
# for video in py.videos:
#     video.streams.first().download()
