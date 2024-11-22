from yt_dlp import YoutubeDL
import tkinter as tk

#legg til last ned som mp3

root = tk.Tk()

def lastned():
    lenke = lenken.get()
    with YoutubeDL() as ydl:
        ydl.download(lenke)

overskrift = tk.Label(root, text = "Hva vil du laste ned?", font=("Arial", 24))
overskrift.pack()

lenken = tk.Entry(root)
lenken.pack()

send = tk.Button(root, text = "Last ned", command=lastned)
send.pack()

root.mainloop()
