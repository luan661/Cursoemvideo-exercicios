# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

listadealuno = ['luan', 'lorena', 'luardson', 'luana']
print('Ordem de apresentação: ', sample(listadealuno, k=4))
