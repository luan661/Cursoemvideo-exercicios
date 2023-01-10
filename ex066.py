# Crie um programa que leia números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada. No
# final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

n = n1 = c = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    n1 += n
    c += 1
print(f'Quantos números foram digitados?: {c}')
print(f'E qual a soma entre eles?: {n1}')
