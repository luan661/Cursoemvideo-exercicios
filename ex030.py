# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero_inteiro = int(input('Digite um número para descobrir se é PAR ou IMPAR: '))
soma = numero_inteiro % 2
if soma == 0:
    print('O numero é par!')
else:
    print('O número é impar!')