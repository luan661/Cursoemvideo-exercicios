# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

fim = False
numero1 = int(input('Digite um número para seu cálculo fatorial: '))
d = c = numero1
numero2 = numero3 = 0
while fim == False:
    c = c - 1
    if c == 0:
        numero3 = numero1
        fim = True
    numero2 = c * numero1
    numero1 = numero2
print('Valor fatorial de {} = {}'.format(d, numero3))

# c = numero1
# f = 1
# ####
# f = f * c
# c = c-1