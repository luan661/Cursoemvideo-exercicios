# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
for c in range(0, 7):
    n = int(input('Numero: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Números pares: {sorted(lista[0])}')
print(f'Números ímpares: {sorted(lista[1])}')

# lista = [float()]
# for c in range(0, 7):
#     n = int(input('numero: '))
#     if n % 2 == 0:
#         lista.insert(lista.index(float()), n)
#     else:
#         lista.append(n)
# print(f'Valores pares da lista: {lista[0:lista.index(float())]}')
# print(f'Valores ímpares da lista: {lista[lista.index(float())+1:]}')
