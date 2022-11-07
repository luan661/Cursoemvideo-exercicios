# Faça um programa que leia o peso de cinco Pessoas. No final, mostre qual 
# foi o maior e o menor peso lidos.

maior = 0
maior1 = 0
menor = 0
menor1 = 0
a = 0
b = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da pesoa {}?: '.format(c)))
    maior = maior1
    menor = menor1
    if menor == 0:
        menor = peso
        menor1 = menor
        b = c
    if peso > maior:
        maior1 = peso
        a = c
    elif peso < menor:
        menor1 = peso
        b = c
    print(menor, menor1, maior, maior1)
print('O maior é o {}° peso com {:.1f}kg'.format(a, maior1))
print('O menor é o {}° peso com {:.1f}kg'.format(b, menor1))