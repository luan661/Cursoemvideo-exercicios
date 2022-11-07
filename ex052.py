# Faça um programa que leia um número inteiro e diga se ele é ou não um 
# número primo.

#RESOLUÇÃO GUANABARA

numero = int(5)
tot = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('{}\033[33m'.format(c), end='')
        tot += 1
    else:
        print('{}\033[31m'.format(c), end='')
if tot > 2:
    print('\n\033[mO número {} não é um número primo.'.format(numero))
else:
    print('\n\033[mO número {} é um número primo.'.format(numero))