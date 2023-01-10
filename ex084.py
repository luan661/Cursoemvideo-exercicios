# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em
# uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

listapess = []
pessoas = []
pesomax = []
pesomin = []
totalpessoas = []
max = min = 0
while True:
    listapess.append(input('Nome da pessoa: '))
    listapess.append(float(input('Peso da pessoa: ')))
    pessoas.append(listapess[:])
    listapess.clear()
    sn = input('Quer continuar? (S/N): ')
    if sn in 'Nn':
        break
for p in pessoas:
    totalpessoas.append(p[0])
    if p == pessoas[0]:
        max = min = p[1]
    else:
        if max < p[1]:
            max = p[1]
        if min > p[1]:
            min = p[1]
for nomes in pessoas:
    if nomes[1] == max:
        pesomax.append(nomes[0])
    if nomes[1] == min:
        pesomin.append(nomes[0])
print('=-=' * 30)
print(f'Um total de {len(totalpessoas)} foram cadastradas.')
print(f'Os maiores pesos foram do(a)...{pesomax} com {max:.1f}Kg')
print(f'Os menores pesos foram do(a)...{pesomin} com {min:.1f}Kg')
