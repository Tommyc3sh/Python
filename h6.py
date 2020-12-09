#Christopher Robin Kaasik
#24.11.2020
#IT-20


#faili avamine
minu_fail = open('nimi.txt', 'r')

#faili lugemine
faili_sisu = minu_fail.readlines()

#faili sisu kuvamine
ref = 0
kesk = 0
erakondi_kokku = []
for i in range(len(faili_sisu)):
    enimi, pnimi, ek, sobrad = faili_sisu[i].split(" ")
    if ek=="RE":
        ref+=1
    if ek=="KE":
        kesk+=1
        if ek not in erakondi_kokku:
            erakondi_kokku.append(ek)
    print(f"{enimi:11}{pnimi:10}{ek:4}{sobrad:5}", end="")
    
#lisame andmed uude faili.
with open('poliitikud.txt', 'a') as minu_fail:
    faili_kirjutamiseks.write(enimi+" "+pnimi+"\n")

    
print(f"\n-------------\nreformikaid kokku: {ref}")
print(f"kesikuid_kokku: {kesk}")
print(f"erakondi_kokku: {len(erakondi_kokku)}")

#faili sulgemine
minu_fail.close









