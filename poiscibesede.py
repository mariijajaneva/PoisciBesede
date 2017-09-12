import time
import string
import random



class PoisciBesede:
  
  def __init__(self, visina=10 sirina=12)
    self.visina = visina
    self.sirina = sirina
    self.plosca = []
    for i in range(visina):
      self.plosca[i] = sirina * ["0"]
    print('Ustvarili smo začetno ploščo')
    
  def vrstica(self, index):
    return self.plosca[index]
      
      
  def stolpec(self, index):
    return self.plosca[::][index]
      
     
  def postavitev_besede(beseda, plosca):
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
      
    x = random.randrange(0, xsize)
    y = random.randrange(0, ysize)
    
    for i in xrange(0, len(beseda)):
      plosca[y + d[1] * i][x + d[0] * i] = beseda[i]
    return plosca
  
  plosca = [[random.choice(string.uppercase) for i in xrange(0,sirina)] for j in xrange(0, visina)]
    
  print "\n",join(map(lambda vrstica: " ".join(vrstica), plosca)]
                  
  beseda = ["LUNA", "SLIKE", "OMARA", "OKNO", "OSA", "OGLEDALO", "VREČKA", "SVINČNIK", "ZNAMKA", "KOLEDAR", 
            "FLAŠA", "ZVEZEK", "BATERIJA", "KEMIK", "RAČUNALNIK", "RADIRKA", "ČOKOLADA", "DOM", "ROKOVNIK", 
            "REKA", "VERIŽICA", "KRPA", "MIŠ", "ŠKARJE", "KLOVN", "VODA", "NAŠA", "LEN"]
                
                
                
  

