# Escreva um programa em Python que leia um número inteiro qualquer e peça 
# para o usuário escolher qual será a base de conversão: 1 para binário, 
# 2 para octal e 3 para hexadecimal.

conversor = int(input('Digite um número para converte-lo: '))
escolha = int(input('''
Opção 1 (binário)
Opção 2 (Octal)
Opção 3 (Hexadecimal)
'''))
op1 = ('Seu valor Binário é: {}'.format(bin(conversor)[2:]))
op2 = ('Seu valor Octal é: {}'.format(oct(conversor)[2:]))
op3 = ('Seu valor Hexadecimal é: {}'.format(hex(conversor)[2:]))
if escolha == 1:
    print(op1)
elif escolha == 2:
    print(op2)
elif escolha == 3:
    print(op3)
else:
    print('Opção inválida!. Tente novamente.')