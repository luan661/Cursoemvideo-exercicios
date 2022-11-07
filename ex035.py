# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

print('Digite 3 lados para ver se é possível formar um trângulo.\n')
a = int(input('Lado 1: '))
b = int(input('Lado 2: '))
c = int(input('lado 3: '))
if a + b > c and a + c > b and b + c > a:
    print('Pode ser formado um triângulo')    
else:
    print('Não pode ser formado um triângulo')
