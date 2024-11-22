#ideer:
#ordbok med spørsmål, 1 riktig svar og 3 feil svar
#knapp som lar deg gå til neste spørsmål
#lag poengsum, og vis hvor mange de fikk riktig på slutten (f.eks. 4/5) og knapp som lar deg starte igjen
#og kanskje velge ut random spørsmål så det ikke er de samme hver gang
import tkinter as tk
import random
import json

root = tk.Tk()

with open("quizordbok.json", "r") as fil:
    data = json.load(fil)

root.mainloop()