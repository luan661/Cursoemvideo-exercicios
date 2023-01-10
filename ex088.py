# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O
# programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep

lista = list(range(1, 61))
print(f'{"-"*35}\n{"JOGA NA MEGA SENA":^33}\n{"-"*35}')
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"-="*3}{f" SORTEANDO {n} JOGOS "}{"=-"*3}')
for jogo in range(1, n+1):
    print(f'Jogo {jogo}: {sorted(sample(lista, 6))}')
    sleep(1)
print(f'{"-="*4}{" < BOA SORTE! > "}{"=-"*4}')
