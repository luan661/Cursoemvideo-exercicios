# Faça um programa que leia o sexo de uma pessoa, mas só aceite os 
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até 
# ter um valor correto.

f = 'f'
s = input('Digite seu sexo [M/F]: ')
m = 'm'
while s != m and s != f:
    s = input('Opção inválido! Por favor digite novamente: ')
print('Opção salva!')
