# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do 
# homem mais velho e quantas mulheres têm menos de 20 anos.

a1 = 0
a2 = 0
a3 = ''
contador = 0
idade2 = 0
m = ''
f = ''
for c in range(1, 5):
    nome = input('\nNome {}: '.format(c))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo. Digite "M" para Masculino e "F" para Feminino: '))
    #MÉDIA DE IDADE#
    idade2 = idade + idade2
    #NOME DO MAIS VELHO#
    if sexo == 'm':
        if idade > a1:
            a1 = idade
            a2 = c
            a3 = nome
    #QUANTAS MULHERES#
    elif sexo == 'f':
        if idade < 20:
            contador = contador + 1
print('\nA média de idade do grupo é: {} anos.'.format(idade2 // 4))
print(f'O homem com mais idade é {a3} com {a1} anos.')
print('Mulheres com menos de 20 anos no grupo: {}.\n'.format(contador))