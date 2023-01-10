# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e
# vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

import random
import time


def sorteia():
    '''



    :return:
    '''
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(random.randint(0, 25))
        time.sleep(0.3)
        print(numeros[c], end=' ')
    print('Pronto!')


def somapar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os números pares da lista {numeros}, temos {soma}.')


numeros = []
sorteia()
somapar()

