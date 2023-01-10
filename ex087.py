# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

contador = soma3coluna = maiorlinha2 = pares = 0
lista = [[], [], [], [], [], [], [], [], []]
for a in range(0, 9):
    n = int(input('Número: '))
    lista[a] = n
    if n % 2 == 0:
        pares += n
print('=-=' * 15)
for b in range(0, 9):
    print(f'[{lista[b]:^7}]', end='')
    contador += 1
    if contador == 3:
        print('')
        soma3coluna += lista[b]
        contador = 0
for c in lista[3:6]:
    if c == lista[3]:
        maiorlinha2 = c
    else:
        if c > maiorlinha2:
            maiorlinha2 = c
print('=-=' * 15)
print(f'Soma dos valores pares digitados: {pares}')
print(f'Soma dos valores da 3° coluna: {soma3coluna}')
print(f'O maior valor da 2° liha é: {maiorlinha2}')
