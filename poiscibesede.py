import time
import string
import random



class PoisciBesede:
  
  def __init__(self, visina, sirina):
    self.visina = visina
    self.sirina = sirina
    print('Ustvarili smo začetno ploščo')
    
  def vrstica(self, index):
    vrstica = 0
    for i in range(1,11):
      vrstica += (self.visina) // 10
      print ('vrstica')
      return vrstica
      
      
    
    
  def stolpec(self, index):
    for j in range(1, 13):
      
      
    
    
    
    
  def kvadratek(self, index):
    
    
    
    
  
  def postavitev_besede(beseda, plosca):
    beseda = random.choice([beseda, beseda[::-1]])
    
    d = random.choice([[1,0], [0,1], [1,1]])
    if d[0] == 0:
      xsize = sirina
     else:
      xsize = sirina - len(beseda)
      
    if d[1] == 0:
      ysize = visina
    else:
      ysize = visina - len(beseda)
      
    x = random.randrange(0, xsize)
    y = random.randrange(0, ysize)
    
    for i in xrange(0, len(beseda)):
      plosca[y + d[1] * i][x + d[0] * i] = beseda[i]
    return plosca
  
  plosca = [[random.choice(string.uppercase) for i in xrange(0,sirina)] for j in xrange(0, visina)]
    
  print "\n",join(map(lambda row: " ".join(row), plosca)]
                  
  beseda = ["LUNA", "SLIKE", "OMARA", "OKNO", "OSA", "OGLEDALO", "VREČKA", "SVINČNIK", "ZNAMKA", "KOLEDAR", 
            "FLAŠA", "ZVEZEK", "BATERIJA", "KEMIK", "RAČUNALNIK", "RADIRKA", "ČOKOLADA", "DOM", "ROKOVNIK", 
            "REKA", "VERIŽICA", "KRPA", "MIŠ", "ŠKARJE", "KLOVN", "VODA", "NAŠA", "LEN"]
                
                
                
  

