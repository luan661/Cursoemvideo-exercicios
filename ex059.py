# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opc1 = 0
opc2 = 0
opc3 = 0
opc = int(input(
    '''
    Digite uma das opções abaixo:
    
    [1] Somar os valores.
    [2] Multiplicar os valores.
    [3] Exibir o valor maior.
    [4] Pedir novos números.
    [5] Sair do programa.
    
    Opção: '''
))
while opc == 4:
    print(
        '''
        Refazendo operações...'''
    )
    sleep(2)
    opc = int(input(
        '''
        Digite uma das opções abaixo:

        [1] Somar os valores.
        [2] Multiplicar os valores.
        [3] Exibir o valor maior.
        [4] Pedir novos números.
        [5] Sair do programa.

        Opção: '''
    ))
while opc == 1:
    opc1 = n1 + n2
    print('A somas dos valores {} e {} dá: {}'.format(n1, n2, opc1))
    opc = 0
while opc == 2:
    opc2 = n1 * n2
    print('O valor {} X {} dá um total de {}'.format(n1, n2, opc2))
    opc = 0
while opc == 3:
    opc3 = n1
    if opc3 > n2:
        print('O 1° valor ({}) é maior que o 2° ({}).'.format(n1, n2))
    elif opc3 < n2:
        print('O 2° valor ({}) é menor que o 1° ({}).'.format(n2, n1))
    else:
        print('Os 2 valores são iguais. Não há maior nem menor valor.')
    opc = 0
while opc == 5:
    print('Saindo do programa...')
    sleep(1)
    opc = 0
print('Fim do programa.')
