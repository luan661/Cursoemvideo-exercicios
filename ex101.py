# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas
# eleições.

import datetime


def voto(ano):
    idade = datetime.date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


ano = int(input('Seu ano de nascimento: '))
print(voto(ano))
