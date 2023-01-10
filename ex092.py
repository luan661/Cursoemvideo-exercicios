# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
# aposentar.

from datetime import date

pessoa = {'Nome': str(input('Nome: ')),
          'Ano': int(input('Ano de nascimento: ')),
          'Carteira': int(input('Carteira de trabalho: '))}
if pessoa['Carteira'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = int(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Ano de contratação'] + 35 - pessoa['Ano']
    pessoa['Ano'] = date.today().year - pessoa['Ano']
print('=-=' * 50)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')