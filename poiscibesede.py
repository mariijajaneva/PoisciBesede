import time
import string
import random




class PoisciBesede:
  
  def __init__(self, visina=10, sirina=12):
    self.visina = visina
    self.sirina = sirina
    self.plosca = [sirina*["0"] for i in range(visina)]
    self.abeceda = ["A","B","C","Č","D", "E","F","G","H","I","J","K","L","M","N","O","P","R","S","Š","T","U","V","Z","Ž"]
    print('Ustvarili smo začetno ploščo')
    
  def vrstica(self, index):
    return self.plosca[index]
      
      
  def stolpec(self, index):
    return self.plosca[::][index]
      
     
  def postavitev_besede(self, beseda,stevec=0):
    if stevec == 500:
      return False
    beseda = random.choice([beseda, beseda[::-1]])
    
    d = random.choice([[1,0], [0,1], [1,1]])
    if d[0] == 0:
      xsize = self.sirina
    else:
      xsize = self.sirina - len(beseda)
      
    if d[1] == 0:
      ysize = self.visina
    else:
      ysize = self.visina - len(beseda)

    if xsize == 0:
      x = 0
    else:
      x = random.randrange(0, xsize)

    if ysize == 0:
      y = 0
    else:
      y = random.randrange(0, ysize)

    zmoremo = True

    for i in range(0, len(beseda)):
      kvadratek=self.plosca[y + d[1] * i][x + d[0] * i]
      if  kvadratek == beseda[i] or kvadratek == "0":
        pass
      else:
        zmoremo = False
        
    if zmoremo:
      for i in range(0, len(beseda)):
        self.plosca[y + d[1] * i][x + d[0] * i] = beseda[i]
      return True
    else:
      return self.postavitev_besede(beseda,stevec+1)


  def postavitev_polja(self, besede):
    sez_besed = set()
    for beseda in besede:
      if self.postavitev_besede(beseda):
        sez_besed.add(beseda)
    self.preostale_besede = sez_besed
    for i in range(0,self.visina):
      for j in range(0, self.sirina):
        if self.plosca[i][j] == '0':
          self.plosca[i][j] = random.choice(self.abeceda)
    print (sez_besed)
    print (self)

  def smo_nasli(self, beseda):
    mnozica={beseda,beseda[::-1]}
    if beseda in self.preostale_besede or beseda[::-1] in self.preostale_besede:
      if beseda in self.preostale_besede:
        print("Najdena beseda : {beseda}.".format(beseda = beseda))
      elif beseda[::-1] in self.preostale_besede:
        print("Najdena beseda : {beseda}.".format(beseda = beseda[::-1]))

      self.preostale_besede = self.preostale_besede.difference(mnozica)
      if len(self.preostale_besede) == 0:
        print("Zmagali ste")
      else:
        print("Preostale besede : ")
        print(self.preostale_besede)
        print(self)
    else:
      print("Ne iščemo besede : {beseda} ".format(beseda = beseda) )

  

  def iskanje_besede(self, x1, x2, y1, y2):
    if x2 - x1 < 0:
      return self.iskanje_besede(x2, x1, y1, y2)
    if y2 - y1 < 0:
      return self.iskanje_besede(x1, x2, y2, y1)
    beseda=""
    if x1 == x2:
      for i in range(y2 - y1 + 1):
        beseda += self.plosca[y1 + i][x1]
    elif y1 == y2:
      for i in range(x2 - x1 + 1):
        beseda += self.plosca[y1][x1 + i]
    else:
      if x2 - x1 == y2 - y1:
        for i in range(x2 - x1 + 1):
          beseda += self.plosca[y1 + i][x1 + i]
      else:
        print("Napačno izbrana polja")
    self.smo_nasli(beseda)
      
      
      
    
    
    
  def __repr__(self):
    lplosca=[str(self.vrstica(i)) for i in range(self.visina)]
    return "\n".join(lplosca)    
    
  
                  
besede = ["LUNA", "SLIKE", "OMARA", "OKNO", "OSA", "OGLEDALO", "VREČKA", "SVINČNIK", "ZNAMKA", "KOLEDAR", 
          "FLAŠA", "ZVEZEK", "BATERIJA", "KEMIK", "RAČUNALNIK", "RADIRKA", "ČOKOLADA", "DOM", "ROKOVNIK", 
          "REKA", "VERIŽICA", "KRPA", "MIŠ", "ŠKARJE", "KLOVN", "VODA", "NAŠA", "LEN"]
                
Po = PoisciBesede()
Po.postavitev_polja(besede)

                
  

