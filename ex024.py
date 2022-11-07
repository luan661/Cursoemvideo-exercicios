# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

santo = str(input('Digite um nome de cidade: ')).upper().strip().split()
print('O nome começa com a palavra Santo? {}'.format('SANTO' in santo[0]))
