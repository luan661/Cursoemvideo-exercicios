# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

c = n = 0
while True:
    n = int(input('Digite um número para sua tabuada [Negativo para parar]: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:<2} = {n*c}')
print('Processo finalizado.')
