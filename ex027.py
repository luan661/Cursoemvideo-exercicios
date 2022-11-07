# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome_da_pessoa = str(input('Digite um nome completo: ')).strip().split()
print('Qual é o seu primeiro nome? {}\nE o seu último? {}'.format((nome_da_pessoa[0]),
    (nome_da_pessoa[-1])))
