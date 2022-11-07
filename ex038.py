# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero = int(input('Digite um número: '))
numero2 = int(input('Digite o 2° número: '))
igual = 0
if numero == numero2:
    print('Não existe valor maior, os 2 são iguais.')
    igual = 1
if numero > numero2 and igual == 0:
    print('O primeiro valor é maior - {}'.format(numero))
if numero2 > numero and igual == 0:
    print('O segundo valor é maior - {}'.format(numero2))
