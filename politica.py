import random
class Politica():
   bracos = ["acao", "aventura", "romance", "terror", "infantil"]
   
   def __init__(self,recompensas) -> None:
      self.recompensas = recompensas
      
   def processo(self):
      self.var = random.random()
      if self.var < 0.5:
         bracosAleatorios = random.randint(1,5)
         print(self.bracos[bracosAleatorios])
         print(bracosAleatorios)
      
      self.recompensas[bracosAleatorios] += 1
      print(self.recompensas)
      print(self.var)
recompensas = [1,1,1,1,1]
politica = Politica(recompensas)
#number = random(0,1)
politica.processo()
