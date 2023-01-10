# Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: início, fim e passo. Seu programa tem que realizar três
# contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    print('=-=' * 25)
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo > 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo} '
                  f'(transformados para negativos).')
            for c in range(inicio, fim - 1, -passo):
                print(c, end=' ')
                sleep(0.3)
        elif passo < 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
            for c in range(inicio, fim - 1, passo):
                print(c, end=' ')
                sleep(0.3)
    elif inicio < fim:
        if passo > 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
            for c in range(inicio, fim + 1, passo):
                print(c, end=' ')
                sleep(0.3)
        elif passo < 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo} '
                  f'(transformados para positivos).')
            for c in range(inicio, fim + 1, -passo):
                print(c, end=' ')
                sleep(0.3)
    print('FIM!')


# A)
contador(1, 10, 1)
# B)
contador(10, 0, 2)
# C)
print('=-=' * 25)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
