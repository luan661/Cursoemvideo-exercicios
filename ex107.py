# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que
# importe esse módulo e use algumas dessas funções.

from aula22 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10% temos {moeda.dez(valor)}')
print(f'Reduzindo 13% temos {moeda.treze(valor)}')
