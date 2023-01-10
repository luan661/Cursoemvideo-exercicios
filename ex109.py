# Modifique as funções que form criadas no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou
# não formatado pela função moeda(), desenvolvida no desafio 108.


from aula22 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, False)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, False)}')
print(f'Aumentando 10% temos {moeda.dez(valor, True)}')
print(f'Reduzindo 13% temos {moeda.treze(valor, False)}')
