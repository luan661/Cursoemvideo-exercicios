# Adapte o código do desafio #107, criando uma função adicional chamada
# moeda() que consiga mostrar os números como um valor monetário formatado.


from aula22 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.dez(valor))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.treze(valor))}')
