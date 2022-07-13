#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar considerando 1U$$ = 3.27R$

r = float(input('quantos reais tenho na carteira?: '))
print('então eu tenho {:.2f} em dólares'.format(r / 3.27))
