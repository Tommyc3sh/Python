#christopher robin kaasik
#it20

class Auto:
    #atribuudid
    mark = ""
    aasta = 0
    hind = 0
    v2rv = "määramata"
    maxkiire = 0 
    
    #meetodid
def __init__(self,x,y,z,i,g):
    self.mark = x
    self.aasta = y
    self.hind = z
    self.v2rv = i
    self.maxkiire = g
    
    
    def lisaMark(self, x):
        self.mark = x
        
    
    def lisaAasta(self, y):
        self.aasta = y
    
    
    def lisaHind(self, z):
        self.hind = z
    
    def lisav2rv(self, i):
        self.v2rv = i
    
    def lisamax(self, g):
        self.max = g
    
    def kuva(self):
        print(f"mark: {self.mark}\naasta: {self.aasta}\nhind: {self.hind}")
        print(f"värv: {self.v2rv}\nmaxkiire: {self.maxkiire}km/h")
        
minuauto = Auto("BMW", 2020, 1000, "roostes", 200)
minuauto.kuva() 
        