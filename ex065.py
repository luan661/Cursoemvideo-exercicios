# Crie um programa que leia vários números inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

import random

m = c = contador = menor = n1 = maior = men = mai = 0
n = 1
while n > 0:
    c += 1
    n = int(input('\nDigite um número ou [0] para parar: '))
    maior = n
    if c == 1:
        men = n
        menor = men
        mai = menor
    if maior > mai:
        mai = n
    if n < men:
        men = n
        menor = men
    m += n
print('\nMédia: ', m/c)
#print('menor', menor, 'maior', maior, 'men', men, 'mai', mai)
print('O maior número é: {} e o menor é: {}'.format(mai, menor))

