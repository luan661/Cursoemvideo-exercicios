# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

a = int(input('digite o cateto oposto: '))
b = int(input('digite o cateto adjacente: '))
hipotenusa = hypot(a, b)
print('Hipotenusa = {:.1f}'.format(hipotenusa))
