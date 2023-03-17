from random import uniform

def run(steps, bracos, func_recompensa, politica, verbose=False):
    '''
    steps:       int            Total steps
    bracos:        Array          Lista de bracos e probabilidades
    func_recompensa: function       recompensa Function
    politica:      PoliticaClass    Politica Test
    '''
    
    recompensas = []
    bracos_selecionados = []
    
    # inicializa as recompensas
    for braco, prob in enumerate(bracos):
        politica.update(braco, 0)

    # run env
    for step in range(steps):
        # Seleciona um braço
        braco = politica.act()
        
        # Retorna a recompensa desse braço
        recompensa = func_recompensa(bracos[braco], step=step)
        
        # Update mean recompensa
        politica.update(braco, recompensa)  #fazer o método update na classe Politica
        
        bracos_selecionados.append(braco)
        recompensas.append(recompensa)
        
        if verbose:
            print("{}: braco {} com recompensa {}".format(step, braco, recompensa))
    
    if verbose:
        print("Recompensa Cum: {}".format(np.sum(recompensas))) #o que era pra ser o np?
    
    return bracos_selecionados, recompensas


def recompensando(bracos[braco], step):
    if bracos[braco] == bracos[0]:
        return uniform(0, 0.2)
    elif bracos[braco] == bracos[1]:
        return uniform(0, 0.5)
    elif bracos[braco] == bracos[2]:
        return uniform(0, 0.4)
    elif bracos[braco] == bracos[3]:
        return uniform(0, 1)
    else: 
        return uniform(0, 0.6)
    #ta errado, rever como faz a recompensa

run(50, ["acao", "aventura", "romance", "terror", "infantil"], recompensando(), )

class Politica:
    pass