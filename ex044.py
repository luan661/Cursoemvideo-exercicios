# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor_do_produto = float(14.99)
frase1 = 'Você pagará {}x de R${:.2f}. Tenha um bom dia!\n'
escolha = int(input(
'''
Escolha entre as opções abaixo:

Opção 1: A vista no dinheiro/cheque com 10(%) de desconto.
Opção 2: A vista no cartão com 5(%) de desconto.
Opção 3: Em até 2x no cartão com preço total.
Opção 4: 3x ou mais no cartão com 20(%) de juros.

'''))
if escolha == 3 or escolha == 4:
    vezes = int(input('Em quantas vezes? '))
if escolha == 1:
    print(frase1.format(1, valor_do_produto - (valor_do_produto * (10/100))))
elif escolha == 2:
    print(frase1.format(1, valor_do_produto - (valor_do_produto * (5/100))))
elif escolha == 3:
    print(frase1.format(vezes, valor_do_produto / vezes))
elif escolha == 4:
    print(frase1.format(vezes, (valor_do_produto*(20/100) + valor_do_produto)
    / vezes))
else:
    print('Opção inválida! Tente novamente.')