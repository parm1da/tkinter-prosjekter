import requests
import tkinter as tk
import tkinter.scrolledtext as st
# https://www.geeksforgeeks.org/python-tkinter-scrolledtext-widget/

root = tk.Tk()
root.title("Finn Lyrics")

def hentlyrics():
    artisten = artist.get()
    sangen = sang.get()
    url = f"https://api.lyrics.ovh/v1/{artisten}/{sangen}"
    svar = requests.get(url)
    data = svar.json()
    lyrikk.delete("1.0", "end")
    try:
       lyrikk.insert(tk.INSERT, data["lyrics"])
    except:
        lyrikk.insert(tk.INSERT, "Kunne ikke finne lyrics")


overskrift = tk.Label(root, text="Lyric-Generator")
overskrift.pack()

artistoverskrift = tk.Label(root, text = "Artist")
artistoverskrift.pack()
artist = tk.Entry(root)
artist.pack()

sangoverskrift = tk.Label(root, text = "Sang")
sangoverskrift.pack()
sang = tk.Entry(root)
sang.pack()

send = tk.Button(root, text="Søk", command=hentlyrics, padx = 10, pady = 5)
send.pack(padx = 100)

lyrikk = st.ScrolledText(root, width = 30, height = 8)
lyrikk.pack(padx = 10)


root.mainloop()