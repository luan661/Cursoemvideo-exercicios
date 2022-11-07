# Faça um programa que calcule a soma entre todos os números que são
#  múltiplos de três e que se encontram no intervalo de 1 até 500.

print('\n')
soma = 0
for c in range(3, 500, 3):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
        print(c, end=' ')
print('\n\nA soma de todos os valores ímpares multiplos de 3 é: ', soma)
print('\n')