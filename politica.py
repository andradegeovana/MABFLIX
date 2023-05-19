import random
class Politica():
   bracos = ["acao", "aventura", "romance", "terror", "infantil"]
   
   # Inicializa as recompensas
   def __init__(self, recompensas):
      self.recompensas = recompensas
      self.epsilon = 1

   # Seleciona o braco randomicamente
   def processo(self):
      count = 0
      for i in range(30):
         count += 1
         if count == 10:
            self.epsilon -= 0.1
            count = 0
         # var (numero randomico) recebe um valor aleatorio entre 0 e 1
         self.var = random.random()
         # Se o var for menor que o epsilon, escolhe um braco aleatorio
         if self.var < self.epsilon:
            # Escolhe um braco aleatorio entre todos os bracos
            bracosAleatorios = random.randint(0,4)
            # Da uma recompensa ao braco escolhido
            self.recompensas[bracosAleatorios] += 1
            print(self.bracos[bracosAleatorios])
            print(bracosAleatorios)
         # Se o var for maior que o epsilon, escolhe o braco com a maior recompensa
         elif self.var >= self.epsilon:
            maior = 0 
            # Encontra a melhor recompensa
            for i in range(0,len(recompensas)):
               if recompensas[i] > maior:
                  maior = i 
            bracosAleatorios = maior 
            print("else",self.bracos[bracosAleatorios])
 
         print(self.recompensas)
         print(self.var)
         print("Epsilon = ", self.epsilon)
         print("------------------")

recompensas = [0,0,0,0,0]
politica = Politica(recompensas)
#number = random(0,1)
politica.processo()
