# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime

ano_hj = int(datetime.date.today().year)
calculo_ano = int(input('Digite um ano e descubra se é Bissexto ou não: '))
sim1 = 0
if calculo_ano == 0:
    calculo_ano = ano_hj
if calculo_ano % 4 == 0 and calculo_ano % 100 > 0:
    sim1 = int(1)
if calculo_ano % 4 > 0 and calculo_ano % 400 > 0:
    sim = 0
if calculo_ano % 4 > 0 and calculo_ano % 400 == 0:
    sim = 1
if sim1 == 1:
    print('O ano em questão é bissexto')
else:
    print('O ano não é bisexto')