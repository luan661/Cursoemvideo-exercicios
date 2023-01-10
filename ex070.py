# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

c = soma = maismil = maisbarato = 0
nomemaisbarato = ''
while True:
    c += 1
    produto = str(input(f'Nome do produto {c}: '))
    preco = float(input('Preço: '))
    soma += preco
    if preco > 1000:
        maismil += 1
    if c == 1 or preco < maisbarato:
        maisbarato = preco
        nomemaisbarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]? \n')).strip().upper()[0]
    if continuar == 'N':
            break
print(f'Um total de R${soma:.2f} foi gasto nas compras.')
print(f'Um total de {maismil} produtos custam mais de R$1000.')
print(f'O produto mais barato é {nomemaisbarato.capitalize()} '
      f'custando R${maisbarato}.')
