# MABFLIX

## Anotações:

Funções:
  ◦ init -> inicializa os braços e as recompensas <br />
  ◦ update -> atualiza as recompensas <br />
  ◦ act -> selecionar por probabilidade <br />

Epsilon -> número entre 0 e 1, taxa de algo, porcentagem de vezes que ele escolhe

Epsilon: 
  ◦ número entre 0 e 1 (podemos escolher) <br />
  ◦ é uma variável <br />
  ◦ após uma certa quantidade de execuções, ele decrementa (podemos escolher) <br />

Número randomico:
  ◦ número entre 0 e 1 <br />
  ◦ recebe um novo valor a cada escolha/verificação <br />
  
Processo:
  ◦ se o número random for menor que o epsilon, ele escolhe um braço aleatório <br />
  ◦ se o número random for maior que o epsilon, escolhe o melhor braço (de acordo com a recompensa de cada braço) <br />
