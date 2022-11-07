# Faça um programa que leia o ano de nascimento de um jovem e informe, de 
# acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se 
# é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu 
# programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

data_hj = datetime.date.today().year
data_de_nasc = int(input('Digite sua data de nascimento: '))
idade_atual = data_hj - data_de_nasc
if idade_atual < int(18):
    print('Faltam {} ano(s) para você se alistar! Seu alistamento será em {}.'
    .format(18-idade_atual, data_de_nasc+18))
elif idade_atual > 18:
    print('Já se passaram {} ano(s) da data do alistamento. A data de alista'
        'mento foi em {}.'.format(idade_atual-18, data_de_nasc+18))
else:
    print('Está na hora de se alistar!')
