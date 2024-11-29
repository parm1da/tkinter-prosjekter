import random
import tkinter as tk

spørsmålordbok = {
    "spm1": {
        "tekst": "På søndager i Columbus, Ohio er det ulovlig å selge hva?",
        "riktig": "Cornflakes",
        "feil1": "Alkohol",
        "feil2": "Bønnebøker",
        "feil3": "Støvsugere"
    },
    "spm2": {
        "tekst": "Hva er ulovlig å gjøre på et hotellrom i California?",
        "riktig": "Å skrelle en løk",
        "feil1": "Å be til gud",
        "feil2": "Å høre på musikk etter 18.00",
        "feil3": "Å danse"
    },
    "spm3": {
        "tekst": "I 1992, hva ble 2421 amerikanske personer skadet i hjemmet av",
        "riktig": "Husplanter",
        "feil1": "Badekar",
        "feil2": "Meloner",
        "feil3": "Kjøleskap"
    },
    "spm4": {
        "tekst" : "Hvis du har på deg en svømmedrakt offentlig i Florida, hva er det du ikke har lov til?",
        "riktig": "Å synge",
        "feil1": "Løpe",
        "feil2": "Danse",
        "feil3": "Selge blader"
    },
    "spm5": {
        "tekst": "Hvem var det som fjernet brokkoli fra det hvite hus?",
        "riktig": "George Bush",
        "feil1": "Donald Trump",
        "feil2": "Barack Obama",
        "feil3": "Ronald Reagan"
    },
    "spm6": {
        "tekst": "Hva er den ledende dødsårsaken i Papua New Guinea?",
        "riktig": "Å falle fra trær",
        "feil1": "Bilulykke",
        "feil2": "Å sette mat i halsen",
        "feil3": "Drap"
    },
    "spm7": {
        "tekst": "Hva slags mat kan man lage diamanter av?",
        "riktig": "Peanøttsmør",
        "feil1": "Druer",
        "feil2": "Epler",
        "feil3": "Bananer"
    },
    "spm8": {
        "tekst": "Hvorfor fikk den første regissøren av filmen haisommer sparken?",
        "riktig": "Fordi han hele tiden kalte haien for en hval",
        "feil1": "Fordi han stjal fra skuespillerne",
        "feil2": "Fordi han gikk ut med nazistiske synspunkter i media",
        "feil3": "Fordi han hadde løyet på CV-en."
    },
    "spm9": {
        "tekst": "Hva er den vanligste setningen i Harry Potter-bøkene?",
        "riktig": "«Ingenting skjedde»",
        "feil1": "«Harry Potter kom ned trappa»",
        "feil2": "«Ved Merlins skjegg»",
        "feil3": "«Humlesnurr gikk sakte forbi»"
    },
    "spm10": {
        "tekst": "Hvilket av disse dyrene er minst?",
        "riktig": "Mus",
        "feil1": "Tiger",
        "feil2": "Katt",
        "feil3": "Pytonslange"
    }
}

root = tk.Tk()
midtstillt = tk.Frame(root)
midtstillt.pack()
knapper = tk.Frame(root)
knapper.pack()

posisjoner = [[3,0],[3,1],[4,0],[4,1]]

def nyttspill():
    global poeng
    global ubruktespørsmål
    global spørsmålspurt
    spørsmålspurt = 0
    poeng = 0
    ubruktespørsmål = spørsmålordbok.copy()
    sjekktekst.configure(text= " ")
    fåspørsmål()

def fåspørsmål():
    ubrukteposisjoner = posisjoner.copy()

    tilfeldig  = random.randint(0, len(ubrukteposisjoner)-1)
    posisjon = ubrukteposisjoner[tilfeldig]
    alternativ1.grid(row=posisjon[0], column=posisjon[1])
    ubrukteposisjoner.remove(posisjon)

    tilfeldig = random.randint(0, len(ubrukteposisjoner)-1)
    posisjon = ubrukteposisjoner[tilfeldig]
    alternativ2.grid(row=posisjon[0], column=posisjon[1])
    ubrukteposisjoner.remove(posisjon)

    tilfeldig = random.randint(0, len(ubrukteposisjoner)-1)
    posisjon = ubrukteposisjoner[tilfeldig]
    alternativ3.grid(row=posisjon[0], column=posisjon[1])
    ubrukteposisjoner.remove(posisjon)

    tilfeldig = random.randint(0, len(ubrukteposisjoner)-1)
    posisjon = ubrukteposisjoner[tilfeldig]
    alternativ4.grid(row=posisjon[0], column=posisjon[1])
    ubrukteposisjoner.remove(posisjon)

    spørsmål_id, spørsmål = random.choice(list(ubruktespørsmål.items()))
    ubruktespørsmål.pop(spørsmål_id)
    spørsmålet.configure(text=spørsmål["tekst"])
    alternativ1.configure(text=spørsmål["riktig"], command= lambda : fargesjekk("riktig", alternativ1),fg = "black")
    alternativ2.configure(text=spørsmål["feil1"], command= lambda : fargesjekk("feil", alternativ2),fg = "black")
    alternativ3.configure(text=spørsmål["feil2"], command= lambda : fargesjekk("feil", alternativ3),fg = "black")
    alternativ4.configure(text=spørsmål["feil3"], command= lambda : fargesjekk("feil", alternativ4),fg = "black")

def fargesjekk(riktigellerfeil, alternativ):
    alternativ1.configure(fg="green")
    if riktigellerfeil == "feil":
        alternativ.configure(fg="red")
    sjekk(riktigellerfeil)

def sjekk(riktigellerfeil):
    global poeng
    global spørsmålspurt
    spørsmålspurt += 1
    if riktigellerfeil == "riktig":
        poeng += 1
        sjekktekst.configure(text = f"Riktig! {poeng}/5")
    elif riktigellerfeil == "feil":
        sjekktekst.configure(text = f"Feil! {poeng}/5")
    root.after(1000, ettersjekk)

def ettersjekk():
    if spørsmålspurt < 5:
        fåspørsmål()
    elif spørsmålspurt >= 5:
        spillferdig()

def spillferdig():
    global poeng
    global spørsmålspurt
    spørsmålet.configure(text=f"Du fikk {poeng}/5 poeng. Spill igjen?")
    # sjekktekst.pack_forget()
    alternativ1.grid_forget()
    alternativ2.grid_forget()
    alternativ3.grid_forget()
    alternativ4.grid_forget()
    poeng = 0
    spørsmålspurt = 0

overskrift = tk.Label(midtstillt, text="Quiz!", font=("Arial", 24))
overskrift.pack()

spørsmålet = tk.Label(midtstillt)
spørsmålet.pack()

alternativ1 = tk.Button(knapper, height = 5, width = 25)
alternativ2 = tk.Button(knapper, height = 5, width = 25)
alternativ3 = tk.Button(knapper, height = 5, width = 25)
alternativ4 = tk.Button(knapper, height = 5, width = 25)

sjekktekst = tk.Label(midtstillt)
sjekktekst.pack()

startknapp = tk.Button(midtstillt, text = "Ny Quiz", command=nyttspill, height = 2)
startknapp.pack()
 
root.mainloop()