# Crie um programa que vai gerar cinco números aleatórios e colocar em uma
# tupla. Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.

import random

b = tuple()
for c in range(0, 5):
    numeros = random.randint(1, 25)
    a = (numeros,)
    b += a 
print('Números gerados: ', b)
print('O maior da lista: {}'.format(max(b)))
print(f'O menor da lista: {min(b)}')
