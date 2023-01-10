# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = np = tuple()
first = c = 0
for c in range(0, 4):
    n1 = int(input('digite um valor: '))
    n += (n1,)
    if n1 % 2 == 0:
        np += (n1,)
    if n1 == 3:
        first = n.index(3)+1
print(f'\nLista: {n}')
if first != 0:
    print(f'A primeira ocorrencia do 3 foi na posição: {first}')
else:
    print(f'Não existe o 3 na lista.')
print(f'O número 9 aparece {n.count(9)} vezes.')
print(f'Os valores PARES da lista são: {np}')
