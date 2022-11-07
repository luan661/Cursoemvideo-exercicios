# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e 
# quantas já são maiores.

import datetime

a = 0
b = 0
for c in range(1, 8):
    nasc = int(input('Ano de nascimento: '))
    yeartoday = datetime.date.today().year
    nasc = yeartoday - nasc
    if nasc >= 18:
        a += 1
    else:
        b += 1
print('O número de pessoas de maiores é: {}'
    '\nO número de pessoas que não atingiram a maioridade é: {}'
    .format(a, b))
