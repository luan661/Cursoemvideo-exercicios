#faça um programa que leia a largura e altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.

pa = float(input('Quanto em altura? (m): '))
pl = float(input('Quanto em largura? (m): '))
pq = pa * pl
t = pq / 2
print('Você vai usar {} litros de tinta para pintar.'.format(t))