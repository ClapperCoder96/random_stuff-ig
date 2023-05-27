import tkinter as tk
from tkinter import *
from pytube import YouTube
import os 
 
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()


l = Label(canvas, text = "Input your video link to download")
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
n = Label(canvas, text = "Input your video link to convert to audio")
n.config(font =("Courier", 14))
n.pack()
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

b = Button(canvas,text='okay',command=download)
b.pack(side='bottom') 


tk.mainloop()
