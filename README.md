# MABFLIX

## Anotações:

Funções:
  ◦ init -> inicializa os braços e as recompensas
  ◦ update -> atualiza as recompensas
  ◦ act -> selecionar por probabilidade

Epsilon -> número entre 0 e 1, taxa de algo, porcentagem de vezes que ele escolhe

Epsilon: 
  ◦ número entre 0 e 1 (podemos escolher)
  ◦ é uma variável
  ◦ após uma certa quantidade de execuções, ele decrementa (podemos escolher)

Número randomico:
  ◦ número entre 0 e 1 
  ◦ recebe um novo valor a cada escolha/verificação
  
Processo:
  ◦ se o número random for menor que o epsilon, ele escolhe um braço aleatório
  ◦ se o número random for maior que o epsilon, escolhe o melhor braço (de acordo com a recompensa de cada braço)
