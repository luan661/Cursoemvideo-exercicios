# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
#
#### RESOLUÇÃO GUANABARA ####


lista = []
p1 = p2 = list()
max = min = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor {c+1}: ')))
    if c == 0:
        max = min = lista[c]
    else:
        if lista[c] > max:
            max = lista[c]
        if lista[c] < min:
            min = lista[c]
print('Valores digitados: ', lista)
for d in range(0, 5):
    if lista[d] == max:
        p1 = p1 + [d+1]
    if lista[d] == min:
        p2 = p2 + [d+1]
print(f'O maior valor digitado foi {max} na posição: {p1}')
print(f'O menor valor digitado foi {min} na posição: {p2}')
