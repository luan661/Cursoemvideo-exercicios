# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

numerofloat = float(input('Digire um número real: '))
print('Sua porção inteira é: {}'.format(math.floor(numerofloat)))