import tkinter as tk

poeng = 0
def cookiefunksjon(verdi):
    global poeng
    poeng += verdi
    poengtekst.configure(text = f"Klikk: {int(poeng)}")
    if poeng > 50 and poeng < 100:
        gratulerertekst.configure(text=f"Flott!!")
    elif poeng > 100 and poeng < 500:
        gratulerertekst.configure(text=f"WOW!!!!")
    elif poeng > 500 and poeng < 1000:
        gratulerertekst.configure(text=f"OMG!!!!!!!!")
    elif poeng > 1000:
        gratulerertekst.configure(text="Du kan stoppe nå...")
    if poeng > pris:
        upgrade.configure(state=tk.NORMAL)
    else:
        upgrade.configure(state=tk.DISABLED)


poengperklikk = 1    
pris = 50   
def oppgrader():
    global poeng
    global poengperklikk
    global pris
    if poeng > pris or poeng == pris:
        poeng = poeng - pris
        poengperklikk = poengperklikk*2
        pris = pris*1.2
        upgrade.configure(text=f"Kjøp upgrade for {int(pris)} poeng!")
        dinoppgradering.configure(text=f"Boost: {poengperklikk}x")
        if poeng < pris:
            upgrade.configure(state=tk.DISABLED)
    poengtekst.configure(text = f"Poeng: {int(poeng)}")
root = tk.Tk()
root.title("COOKIECLICKER")


knapp = tk.Button(root, text = "🍪", padx = 30, pady=30, command=lambda : cookiefunksjon(poengperklikk), font=("Arial", 70))
knapp.pack()

poengtekst = tk.Label(root, text = "Poeng: 0")
poengtekst.pack()

gratulerertekst = tk.Label(root, text = "Trykk på knappen for å få poeng!")
gratulerertekst.pack()

upgrade = tk.Button(root, text = "Kjøp upgrade for 50 poeng!", pady = 5, command=oppgrader, state=tk.DISABLED)
upgrade.pack()

dinoppgradering = tk.Label(root, text="Du har ingen oppgraderinger enda.")
dinoppgradering.pack()

root.mainloop()