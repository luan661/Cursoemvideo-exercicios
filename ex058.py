# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random

tentativa = 0
randonnumero = random.randint(1, 10)
guess = int(input('Em qual número eu pensei? '))
while guess != randonnumero:
    guess = int(input('Errou! Tenta denovo: '))
    tentativa += 1
print('Acertou! N° de tentativas falhas: {}'.format(tentativa))
