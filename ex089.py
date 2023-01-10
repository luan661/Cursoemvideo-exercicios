# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de
# cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.
#
# ###resolução guanabara###

lista = []
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('1° Nota: '))
    nota2 = float(input('2° Nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = input('\nQuer continuar? (S/N): ')
    print('')
    if continuar in 'Nn':
        break
print('-'*50)
print(f'{"N°":<4}{"NOME":<15}{"MÉDIA":>16}')
print('-'*50)
for i, n in enumerate(lista):
    print(f'{i:<4}{n[0]:<15}{n[2]:>16}')
print('-'*50)
while True:
    notas = int(input('Mostrar notas de qual aluno? (0 para iterromper): '))
    print('-'*50)
    print(f'As notas do(a) aluno(a) {lista[notas][0]} são'
          f' {lista[notas][1]}')
    if notas == 0:
        break
print('-'*50)
print('Fim do programa. Tenha um bom dia!')

