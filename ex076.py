# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.
 
print('{}'.format('-'*40))
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('{}'.format('-'*40))
produtos = ('lápis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo',
            25.00, 'transferidor', 9.99, 'mochila', 120.32, 'canetas', 22.30,
            'livro', 34.90)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}'.capitalize(), 'R$ ', end='')
    print(f'{produtos[c+1]:>6}')
print('{}'.format('-'*40))
