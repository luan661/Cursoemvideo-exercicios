# Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag).

cont = 1
soma = cont2 = 0
while cont > 0:
    cont = int(input('Digite um número: '))
    soma = cont + soma
    cont2 += 1
    if cont == 999:
        soma -= 999
        cont = 0
        cont2 = cont2-1
print('Foi digitado {} números com a soma entre eles no valor de {}.'.
      format(cont2, soma))

