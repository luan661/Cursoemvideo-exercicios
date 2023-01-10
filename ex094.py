# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dic = dict()
lis = list()
soma = c = 0
while True:
    dic['Nome'] = str(input(f'Nome {c+1}: ')).capitalize()
    dic['Sexo'] = input('Masculino ou feminino? ').lower()
    dic['idade'] = int(input('Idade: '))
    lis.append(dic.copy())
    dic.clear()
    continuar = str(input('Quer continuar? (S/N): '))
    c += 1
    if continuar in 'Nn':
        break
print('=-=' * 35)
print(f'Um total de {len(lis)} pessoas foram cadastradas.')
for valor in range(0, len(lis)):
    soma += (lis[valor]["idade"])
print(f'A média de idade do grupo: {soma / c} anos.')
print('Lista de mulheres: ', end=' ')
for valor in lis:
    if valor["Sexo"] in 'Ff':
        print(valor["Nome"], end='...')
print('')
print('Pessoas com idade acima da média: ', end='')
for idades in lis:
    if idades['idade'] > soma / c:
        print(idades["Nome"], end='...')
print('')
print('=-=' * 35)
print('Fim.')
