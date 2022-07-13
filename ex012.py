#faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('preço do fogão: R$'))
print('comprando a vista você recebe 5% de desconto, e o valor passa a ser: R${:.2f}'.format(p * 0.95))