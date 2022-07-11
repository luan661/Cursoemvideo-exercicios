#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n = float(input('nota 1 do aluno: '))
n2 = float(input('nota 2 do aluno: '))
n3 = (n + n2) / 2
print('com as notas {:.1f} e {:.1f} o aluno atingiu uma média de {:.1f} em pontos'.format(n, n2, n3))
