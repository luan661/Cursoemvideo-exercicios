#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kilometro = float(input('Quantos kilômetros o carro percorreu?: '))
dias = float(input('Por quantos dias?: '))
preço = ((dias * 60) + (kilometro * 0.15))
print('O valor total do uso fica em R${}'.format(preço))
