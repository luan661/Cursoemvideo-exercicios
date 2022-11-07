# Desenvolva um programa que leia seis números inteiros e mostre a soma
#  apenas daqueles que forem pares. Se o valor digitado for ímpar,
#  desconsidere-o.

n = 0
d = 0
for c in range(1, 7):
    n = int(input('Digite o número {}: '.format(c)))
    if n % 2 == 0:
        d = d + n
if d == 0:
    print('Não há soma pois não foi citado números PARES.')
else:
    print('A soma dos números PARES acima pedidos dá: {}'.format(d))