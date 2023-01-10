# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

c = d = m = f = 0
while True:
    c += 1
    idade = int(input(f'Idade da pessoa {c}: '))
    sexo = input('Sexo da pessoa: ').upper().strip()[0]
    while sexo not in 'FM':
        sexo = input('Sexo da pessoa: ').upper().strip()[0]
    continuar = input('Quer continuar[S/N]? \n').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Quer continuar[S/N]? \n').upper().strip()[0]
    if idade > 18:
        d += 1
    if sexo in 'M':
        m += 1
    if sexo in 'F':
        if idade < 20:
            f += 1
    if continuar in 'N':
        print(f'{d} Pessoas tem mais de 18 anos.')
        print(f'{m} Homens foram cadastrados.')
        print(f'{f} Mulheres tem menos de 20 anos.')
        print('Cadastros finalizados.')
        break