import random
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

base = Tk()
base.geometry("200x150")

a = Label(base, text="6pime liitmist")
a.pack()

contrive = Frame(base, width=450, height=500)
contrive.pack()
silt = Label(base, text="vastus: ")
silt.pack()
suv1 = random.randint(0,10)
suv2 = random.randint(0,10)
liitmine = suv1 + suv2
sisestus = Entry(base)
sisestus.pack()
 
def arvutus(s1, s2):
    kysimus = str(s1)+"+"+str(s2)+"= ?"
    character_frame = Label(contrive, text=kysimus)
    character_frame.pack()
    nupp1 = tkinter.Button(base, text="kontrolli", width=10, command=kontroll)
    nupp1.pack()
def kontroll():
    print(suv1, suv2)
    muutuja = int(sisestus.get(suv1, suv2))
    print(muutuja)
    if liitmine==muutuja:
        print("õige")
    else:
        print("vale")

    
    

    

base.after(0, arvutus(suv1, suv2))
base.mainloop()