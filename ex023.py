# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numeross = 10000
numeros = int(input('Digite um número de 0 a 9999: '))
numeros = numeross + numeros
numerotext = str(numeros)
numerotext = list(numerotext)
print(numerotext)
print('Unidade: {}'.format(numerotext[-1]))
print('Dezena: {}'.format(numerotext[-2]))
print('Centena: {}'.format(numerotext[-3]))
print('Milhar: {}'.format(numerotext[-4]))
