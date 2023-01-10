# Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a área
# do terreno.

def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m².')


# conta
print(f'{"Controle de Terrenos":^30}')
print('-'*30)
n1 = float(input('Lagura (m): '))
n2 = float(input('Altura (m): '))
area(n1, n2)
