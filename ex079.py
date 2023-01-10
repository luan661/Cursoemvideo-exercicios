# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em
# ordem crescente.

lista1 = []
lista2 = []
c = 0
while True:
    lista1.append(int(input('Digite um número: ')))
    if lista1[c] not in lista2[:]:
        lista2.append(lista1[c])
    else:
        print('Valor duplicado! Não vou adicionar...  ')
    c += 1
    ss = input('Quer continuar? ')
    if ss in 'Nn':
        break
print(f'Valores adicionados, em orgem crescente: {sorted(lista2)}')
