# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input('Digite a nota 1: '))
nota_2 = float(input('Digite a nota 2: '))
cálculo = float(nota_1 + nota_2) / 2
print('Média: ', cálculo)
if cálculo < 5.0:
    print('REPROVADO!')
elif 7.0 > cálculo > 4.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
