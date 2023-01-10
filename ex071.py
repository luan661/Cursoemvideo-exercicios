# Crie um programa que simule o funcionamento de um caixa eletrônico. No
# início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

while True:
    valor = int(input('Valor a ser sacado: R$'))
    total, cinquenta = valor - ((valor // 50) * 50), valor // 50
    total, vinte = total - ((total // 20) * 20), total // 20
    total, dez = total - ((total // 10) * 10), total // 10
    um = total // 1
    break
if cinquenta >= 1: print(f'Total de {cinquenta} cédulas de R$50.')
if vinte >= 1: print(f'Total de {vinte} cédulas de R$20.')
if dez >= 1: print(f'Total de {dez} cédulas de R$10.')
print(f'Total de {um} cédulas de R$1.')
