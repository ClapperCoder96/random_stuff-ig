#this is an extremely basic program to download youtube videos or convert them to audio 

from pytube import YouTube 
import os 

#enter mp3 or mp4 for this
choose = input("Are you downloading this video or coverting it to audio? ").lower()

if choose == "mp4":
    link = input("Enter your link: ")
    yt = YouTube(link)
    yt.streams.get_highest_resolution().download()
    print("Download Succsessful")
 
elif choose == "mp3":
    link = input("Enter the link you want to download: ")
    yt = YouTube(link)
    whenyoudontknowwhattonameurvar = yt.streams.filter(only_audio=True).get_audio_only()
    whenyoudontknowwhattonameurvar.download()
    print("Download Succsessful:")
else: 
    print("Please complete the question with either mp4(video) or mp3(audio)")
