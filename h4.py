#Christopher Robin Kaasik
#24.11.2020
#IT-20
import random


#ruutude ja kuupide tabel

for i in range (1,14):
    print(f"{i:4}\t{i:4}\t{i:4}")







#pank

print("*********************************")
print("************  pank   ************")
print("************ €€€€€€  ************")
print("*********************************")
#algarv
konto = 10000
aastad = 5
intress = 0.05

print("aasta  algsumma      intress      kokku")
for i in range(aastad):
    alg = konto
    konto = round(konto+(konto*intress),2)
    print(f"{i+1} {alg:13} {intress*alg:11} {konto:11}")





print("-------------------------------")



#arvamismäng
print("*********************************")
print("********* arvamismäng ***********")
print("********* only 2.99$ ************")
print("*********************************")

arvamised = 0
kordade_arv = 3

suvarv = random.randint(1,6)

while arvamised<kordade_arv:
    arvamised = arvamised+1
    arva = int(input("arva ära vahemikus 1-5: "))
    if arva == suvarv:
        print("win!")
    else:
            print("try again!")
    if arvamised == kordade_arv:
        print("lose")
    print("game over")



input()








#viisikud
for i in range(1,101):
    if i%5==0:
        print(i)
#korrutamis tabel
for i in range (1,11):
    print (f"5 x {i} = {5*i}")

#paaris või paaritu



#suvaline lotonumber
print("tänased lotonumbrid on: ", end="")
for i in range (5):
    suvarv = random.randint(0,9)
    print(suvarv , end="")





#kahanev 3nurk
maks = 6
for i in range (1,maks):
    print((maks-i)*"*")


#kasvav 3nurk
for i in range (1,6):
    print("*"*i)

#tabel tärnidega 1 - 26
for i in range (1,26):
    print("* ", end="")
    #end kõpetab rea
    jaak = i%5
    if jaak==0:
        print("", end="\n")






#müük

#hind = int(input("sisesta oma toote hind: "))
#if hind <= 10:
#    allahind 0.1
#else:
#    allahind 0.2
#summa = hind-hind*allahind
#
#print(summa)


#jalgpall

#sugu = print("sisesta oma sugu M/N: ")
#vanus = int(print("sisesta oma vanus: "))

#if 16>vanus<18





#juubel

synniaasta = int(input("sisesta sünniaasta: "))
vanus = 2020 - synniaasta
jaak = vanus
if vanus%5==0:
    print("sul on juubel")
else:
    print("sul ei ole juubel")














#matemaatika
arv1 = int(input("sisesta nr1"))
arv2 = int(input("sisesta nr2"))
tehe = input("vali tehte märk + - * / ")
if tehe=="+":
    v=nr1+nr2
elif tehe=="-":
    v=nr1-nr2
elif tehe=="*":
    v=nr1*nr2
elif tehe=="/":
    v=nr1/nr2
    
print(f"{nr1}{tehe}{nr2}={v}")







#ruut
kylg1 = input("sisesta ruudu 1. kylg: ")
kylg2 = input("sisesta ruudu 2. kylg: ")
if kylg1==kylg2:
    print("võrdsed")
else:
    print("tegemist ei ole ruuduga mees")

