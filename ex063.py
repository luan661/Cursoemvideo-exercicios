# Escreva um programa que leia um número N inteiro qualquer e mostre na
# tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

c = int(input('Quantos valores Fibbonaci deseja ver? '))
n1, n2 = 0, 1
while c > 0:
    n2 = n1 + n2
    n1 = n2 - n1
    c -= 1
    print(n1, end=' ')
print('Fim do programa.')
