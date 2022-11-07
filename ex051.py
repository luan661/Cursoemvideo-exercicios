# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
4
termo = int(input('\nDigite o termo (começo): '))
razão = int(input('Digite a razão (De quanto em quanto): '))
print('Último termo = {}'.format(termo+(10-1)*razão))
for c in range(termo, (termo+((10-1)*razão))+razão, razão):
    print(c, end=' = ')
print('\n')