import random
class Politica():
   bracos = ["acao", "aventura", "romance", "terror", "infantil"]
   
   # Inicializa as recompensas
   def __init__(self, recompensas):
      self.recompensas = recompensas
      
   # Seleciona o braco randomicamente
   def processo(self):
      for i in range(10):
         # var (numero randomico) recebe um valor aleatorio entre 0 e 1
         self.var = random.random()
         # Se o var for menor que o epsilon, escolhe um braco aleatorio
         if self.var < 0.5:
            # Escolhe um braco aleatorio entre todos os bracos
            bracosAleatorios = random.randint(0,4)
            self.recompensas[bracosAleatorios] += 1
            print(self.bracos[bracosAleatorios])
            print(bracosAleatorios)
         elif self.var >= 0.5:
            maior = 0 
            for i in range(0,len(recompensas)):
               if recompensas[i] > maior:
                  maior = i 
            
            bracosAleatorios = maior 
            print("else",self.bracos[bracosAleatorios])


            
            
            
            
         # Da uma recompensa ao braco escolhido
         
         print(self.recompensas)
         print(self.var)

recompensas = [0,0,0,0,0]
politica = Politica(recompensas)
#number = random(0,1)
politica.processo()
