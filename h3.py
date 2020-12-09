#Christopher Robin Kaasik
#24.11.2020
#IT-20



#tundide ajad
algus = input(" sisesta algusaeg  (hh:mm): ") 
l6pp = input(" sisesta l6ppaeg (hh:mm): " ) 
hh1, mm1 = algus.split(":")
hh2, mm2 = l6pp.split(":")
min1 = int(hh1)*60+int(mm1)
min2 = int(hh2)*60+int(mm2)
vahe = min2-min1
tund = vahe//60
minut = vahe%60
print(f" päeva pikkus on {tund}:{minut}. ")









#emaili kontrollimine
email = input("sisesta email")
print("@" in email)


#vandumine
ropp = input("ära siin vannu: ")
ropp = (ropp.lower()).replace("kurat", "hull mees")
print(ropp) 



#korralik nimi
#nimi = input("sisesta nimi")

#nimi = (nimi.strip()).capitalize()

#print(nimi)


