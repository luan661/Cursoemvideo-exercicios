# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.


def maior(* valor):
    max = 0
    print('=-=' * 25)
    print('Analizando os valores passados...')
    for c in valor:
        print(f'\033[32m{c}\033[m', end=', ')
        if c == valor[0] or c > max:
            max = c
    print(f'\nForam informados \33[31m{len(valor)}\033[m valores '
          f'ao todo.')
    print(f'O maior valor informado foi \033[31m{max}\033[m')


# valores chamados de 1 a 20 com 1 a 50 de tamanho
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('\nFIM')
# valores = list()
# cópia = ()
# for c in range(0, 5):
#     tamanho = random.randint(0, 20)
#     for d in range(0, tamanho):
#         valores.append(random.randint(0, 50))
#     cópia = valores[:]
#     valores.clear()
#     maior(cópia)
# print('\nFIM')
