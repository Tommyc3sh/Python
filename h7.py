#christopher robin kaasik
#IT-20





#ruumalade leidmise programm

def minuApp():
    print("************* ruumala leidmine v1 ***************")
    print("vali kujund\n1 kuup\n2 kera\n3 koonus\n4 silinder\n0 Sulge programm")
    print("*************************************************")
    valik = int(input("sisesta kujundi nimi mida soovite: "))
    if valik==1:
        kuup()
    elif valik==2:
        print(f"kuubi ruumala)
    elif valik==3:
        koonus()
    elif valik==4:
        silinder()
    else:
        return valik
    
    def kuup():
        print("leian kuubi")
        
    x = int(input("sisesta kylg 1: "))
    y = int(input("sisesta kylg 2: "))
    z = int(input("sisesta kylg 3: "))
    v = x * y * z
return v
        
    def kera():
        print("leian kera")
        
        
        
    def koonus():
        print("leian koonus")
        
    def silinder():
        print("leian silindri")
#käivitab programmi tsükkli
        
loop = 1
while loop==1:
    minuapp()
    v = minuapp()
    if v==0:
        loop=0

print("programmi lõpp")
        
        
def kuup():
    print("leian kuubi")
    x = int(input("sisesta kylg 1: "))
    y = int(input("sisesta kylg 2: "))
    z = int(input("sisesta kylg 3: "))
    v = x * y * z
return v
    

#funktsiooni loomine
"""def tervita(keel ="ge"):
    'tervita nime järgi'
    if keel=="et":
        nimi = input("sisesta siia oma nimi: ")
        return "tere "+nimi+"!"
    elif keel=="en":
        nimi = input("enter your name here: ")
        return "Hi "+nimi+"!"
    else:
        nimi = input("Gib deinen namen: ")
        return "hallo "+nimi+"!"

print(tervita(""))"""

#tere, hi, hallo


