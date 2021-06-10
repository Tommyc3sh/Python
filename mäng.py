#christopher robin kaasik
#it20
import random
#kysinb kas tahab mängida
answer = input("tahad mängida ? (y/n): ")
#vahet pole kas paned suure tähega või väikesega
if answer.lower().strip() == "y":
    #proloog
    answer = input ("saabud ristteele, tahad minna '1'(paremale) või '2' (vasakule)?: ")
    if answer == "2":
        answer = input("saabus su ette koletis, tahad '1'(jookse) või '2'(võitle)?: ")
        #võitlus
        if answer == "võitle":
            print("koletis oli sinu jaoks liiga tugev, kaotasid!")
        else:
            print("hea mõte, pääsesid puhta nahaga!")
            
            answer = input(f"kõnnid kaua, on pime näed kaugel tulesid, see tähendab et seal asub linn kus saaks puhata. Kas tahad minna või püsida koha peal? (mine/püsi): ")
        #    
        if answer == "mine":
            print("lähened linnale")
        else:
            print("sa jäid ööseks välja, külmusid surnuks. Mäng Läbi")
                     
    elif answer == "1":
        print("sa oled väsinud, sul on külm ja silmad on vaevu lahti aga sa ei taha alla anda, sa kõnnid ja kõnnid kuni tuleb kari hunte põõsastest välja ja söövad su ära. Mäng läbi")
        
#mõõga atribuudid        
dmg = 25
sword = random.randint(10,50)
mhealth = 100
ehealth = 100
lvl = 1
lives = 1

while (ehealth>=0 and mhealth>=0) or lives==1:
    ehit = random.randint(1,10)
    if ehit==1:
        ehealth = ehealth-random.randint(5,10)
        #prindib 
        mhit = random.randint(1,3)
        if mhit==1:
            mhealth = mhealth-random.randint(1,2)
        print(f"elud: {ehealth}")
        print(f"elud: {mhealth}")
        if mhealth>ehealth:
            print("Võit!!")
            ehealth = 1
            mhealth = 1
        else:
            print("kaotus")
            lives = 0

    
        