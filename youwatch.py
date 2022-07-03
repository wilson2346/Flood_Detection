from pytube import YouTube
path = "./video/"
link = "https://www.youtube.com/watch?v=CgVRnrk4Rv8&t=2706s"
yt = YouTube(link)
yt.streams.get_highest_resolution().download() 