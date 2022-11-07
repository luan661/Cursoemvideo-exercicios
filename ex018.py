# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

angulo = float(input('Digite um ângulo: '))
angulo2 = radians(angulo)
print('Seu seno é: {:.4f}\nSeu cosseno é: {:.4f}\nSua tangente é: {:.4f}'.format(sin(angulo2),
                                                                                 cos(angulo2), tan(angulo2)))
