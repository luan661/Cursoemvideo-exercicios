# Escreva um programa para aprovar o empréstimo bancário para a compra de uma 
# casa. Pergunte o valor da casa, o salário do comprador e em quantos anos 
# ele vai pagar. A prestação mensal não pode exceder 30% do salário ou 
# então o empréstimo será negado.

valor_da_casa = float(input('Digite o valor da casa: '))
salário_do_comprador = float(input('Digite o salário do comprador: '))
em_quantos_anos = int(input('Em quantos anos?: '))
anos_2 = em_quantos_anos * 12
print(anos_2)
prestação = valor_da_casa / anos_2
print(prestação)
salario_final = salário_do_comprador * (30 / 100)
print(salario_final)
if salario_final > prestação:
    print('''Você pagará {} parcelas de R${:.2f} no valor de R${}'''.format(
        anos_2, prestação, valor_da_casa
    ))
    print('Tenha um ótimo dia!')
else:
    print('Compra muito acima do valor de mensalidade.\nTente novamente com um valor maior')