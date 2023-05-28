#A much more advanced version of my YouTube downloader which is more user friendly and is in tkinter 

import tkinter as tk
from tkinter import *
from pytube import YouTube
import os 
 
canvas = Tk()
canvas = Canvas(canvas, bg="pink", width=700, height=200)
canvas.pack()

l = Label(canvas,bg="pink", text="Would you like to download or convert to audio: ")
l.config(font=("Comic Sans", 16))
l.pack()
global p
p = tk.Entry(bg="pink")
p = Entry(canvas)
p.pack()
p.focus_set()
def on_button():
    canvas.winfo_children()[2].destroy()
    if p.get() == "download":
        l = Label(canvas, bg="pink", text="Please input your video link that you would like to download")
        l.config(font =("Comic sans", 14))
        l.pack()
        def download(): 
            #fix this:
            string = e.get() 
            yt = YouTube(string)
            yt.streams.get_highest_resolution().download()
            print("Download Succsessful")
        e = tk.Entry(bg="pink")
        e = Entry(canvas)
        e.pack()
        e.focus_set()
        b = Button(canvas,text='Finish',bg="pink", command=download)
        b.pack(side='bottom') 
    elif p.get() == "audio":
        l = Label(canvas,bg="pink", text="Please input your video link that you would like to convert")
        l.config(font =("Comic Sans", 14))
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
        b = Button(canvas,text='Finish', bg="pink", command=audio)
        b.pack(side='bottom') 
    else:
        l = Label(canvas, bg="pink", text="please input either 'download' or 'audio' in the box\n Please try again")
        l.config(font=("Comic Sans", 14))
        l.pack()
button = tk.Button(canvas, text="Enter",bg="pink", command=on_button)
button.pack()
tk.mainloop()
