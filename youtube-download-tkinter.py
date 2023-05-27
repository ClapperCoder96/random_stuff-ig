#A much more advanced version of my YouTube downloader which is more user friendly and is in tkinter
#STILL IN WORK#

import tkinter as tk
from tkinter import *
from pytube import YouTube
import os 
 
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()

choose = input("Would you like to download or convert to audio: ").lower()
if choose == "download":
    l = Label(canvas, text="Please input your video link that you would like to download")
    l.config(font =("Courier", 14))
    l.pack()
    def download():
        
        global e
        string = e.get() 
        yt = YouTube(string)
        yt.streams.get_highest_resolution().download()
        print("Download Succsessful")
    e = Entry(canvas)
    e.pack()
    e.focus_set()
elif choose == "audio":
    l = Label(canvas, text="Please input your video link that you would like to convert")
    l.config(font =("Courier", 14))
    l.pack()
    def audio():
        global e 
        string = e.get()
        yt = YouTube(string)
        whenyoudontknowwhattonameurvar = yt.streams.filter(only_audio=True).get_audio_only()
        whenyoudontknowwhattonameurvar.download()
        print("Download Succsessful:")
    e = Entry(canvas)
    e.pack()
    e.focus_set()

b = Button(canvas,text='okay',command=choose)
b.pack(side='bottom') 


tk.mainloop()
