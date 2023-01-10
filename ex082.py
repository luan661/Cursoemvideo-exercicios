# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
# conteúdo das três listas geradas.

lista1 = []
lista2 = []
lista3 = []
while True:
    n = int(input('Digite um número: '))
    lista1.append(n)
    continuar = input('Quer continuar? (S/N): ')
    if continuar in 'Nn':
        break
for c in lista1:
    if c % 2 == 0:
        lista2.append(c)
    else:
        lista3.append(c)
print(f'A lista: {lista1}')
print(f'A lista com números pares: {lista2}')
print(f'A lista con números ímppares: {lista3}')
