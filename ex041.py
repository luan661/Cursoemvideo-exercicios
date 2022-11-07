# A Confederação Nacional de Natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

import datetime

anohj = datetime.date.today().year
anonasc = int(input('Digite sua data de nascimento: '))
categ = anohj - anonasc
q = 'Você está na categoria: '
categoria = ['MIRIM', 'INFANTIL', 'JÚNIOR', 'SÊNIOR', 'MASTER']
if 0 <= categ <= 9:
    print(q, categoria[0])
elif 9 < categ <= 14:
    print(q, categoria[1])
elif 14 < categ <= 19:
    print(q, categoria[2])
elif 19 < categ <= 25:
    print(q, categoria[3])
else:
    print(q, categoria[4])