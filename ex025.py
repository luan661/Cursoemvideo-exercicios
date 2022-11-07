# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite um nome completo: ')).strip().upper().split()
print('Existe a palavra "silva" nesse nome? {}'.format('SILVA' in nome))
