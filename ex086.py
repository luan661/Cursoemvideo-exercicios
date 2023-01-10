# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com
# valores lidos pelo teclado. No final, mostre a matriz na tela, com a
# formatação correta.

contador = 0
lista = [[], [], [], [], [], [], [], [], []]
for a in range(0, 9):
    lista[a] = int(input('Número: '))
print('=-=' * 15)
for b in range(0, 9):
    print(f'[{lista[b]:^7}]', end='')
    contador += 1
    if contador == 3:
        print('')
        contador = 0