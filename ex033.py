# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('adivinhador de número menor e maior.')
numero_1 = int(input('Digite 1° número: '))
numero_2 = int(input('Digite 2° número: '))
numero_3 = int(input('Digite 3° número: '))
menor = numero_1
maior = numero_3
iguais = 0
if numero_2 < numero_3 and numero_2 < numero_1:
    menor = numero_2
    iguais = 1
if numero_3 < numero_2 and numero_3 < numero_1:
    menor = numero_3
    iguais = 1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
    iguais = 1
if numero_1 > numero_2 and numero_1 > numero_3:
    maior = numero_1
    iguais = 1
if iguais == 0:
    print('Não existe valor maior ou menor, todos são iguais.')
else:
    print('o menor é o {}, o maior é o {}'.format(menor, maior))
