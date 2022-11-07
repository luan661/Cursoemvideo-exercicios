# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao ttodo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite um nome completo: '))
nomesplit = nome.split()
print('Nome em maiúsculo: {}\nNome em minúsculo: {}'.format(nome.upper(), nome.lower()))
print('Quantas letras tem esse nome? ({})'.format(len(nome.strip().replace(' ', ''))))
print('Quantas letras tem o primeiro nome? ({})'.format(len(nomesplit[0])))
