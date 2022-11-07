# Escreva um programa que faça o computador "pensar" em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
# escolhido pelo computador. O programa deverá escrever na tela se o usuário 
# venceu ou perdeu.

import random

numero_0_5 = str((int(random.randint(0, 5))))
numero_escolha = str(int(input('Digite um número e veja de acerta (de 0 a 5): ')))
print('O número escolhido foi: {}\nVocê acertou? {}'.format(numero_0_5, 
numero_0_5 in numero_escolha))