from tkinter import *

#akna seaded
aken = Tk()
aken.title("Matemaatiline ülesanne")
aken.iconbitmap("favicon.ico")
aken.geometry("300x200")

def tehted():
    a = int(input("1+2= "))
    b = int(input("1+3= "))
    c = int(input("1+4= "))
    oige = 0
    vale = 0
    if a == 1+2:
        oige += 1
    elif a != 3:
        vale += 1
    if b == 1+3:
        oige += 1
    elif b != 4:
        vale += 1
    if c == 1+4:
        oige += 1
    elif c != 5:
        vale += 1
        
def vastused():
    oige = Label(aken, text="Õiged: ", font=10, fg="green")
    oige.grid(row=11, column=0)
    
    vale = Label(aken, text="Valed: ", font=10, fg="red")
    vale.grid(row=12, column=0)

#tekstid
tehe1 = Label(aken, text="1+1= ", font=10)
tehe1.grid(row=0,column=0)
tehe2 = Label(aken, text="1+2= ", font=10)
tehe2.grid(row=1,column=0)
tehe3 = Label(aken, text="1+3= ", font=10)
tehe3.grid(row=2,column=0)
oige = 0
vale = 0

#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)
sisestus2 = Entry(aken)
sisestus2.grid(row=1,column=1)
sisestus3 = Entry(aken)
sisestus3.grid(row=2,column=1)

ok = Button(aken,text="OK", command=vastused)
ok.grid(row=10, column=1)

# print("Õige: "+str(oige))
# print("Vale: "+str(vale))