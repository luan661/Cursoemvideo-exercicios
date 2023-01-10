# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
c = 0
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar? (S/N): ')
    if continuar in 'Nn':
        break
print(f'Quantidade de números digitados: {len(lista)}')
print(f'Lista de valores digitados em reverso: {sorted(lista, reverse=True)}')
if 5 in lista[:]:
    print(f'O valor 5 esta na lista na posição {lista.index(5)}')
else:
    print('O valor 5 não esta na lista.')
