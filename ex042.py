# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

l1 = int(input('Digite a medida do lado 1: '))
l2 = int(input('Digite a medida do lado 2: '))
l3 = int(input('Digite a medida do lado 3: '))
sim = 'O triângulo é do tipo: '
tipo = ['EQUILÁTERO\n', 'ISÓSCELES\n', 'ESCALENO\n']
if l1 == 0 or l2 == 0 or l3 == 0:
    s = 0
else:
    s = 1
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1 and s == 1:
    print('\nÉ possível criar um triângulo!')
else:
    s = 0
if l1 == l2 == l3 and s == 1:
    print('{}{}'.format(sim, tipo[0]))
elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1 and s == 1:
    print('{}{}'.format(sim, tipo[1]))
elif l1 != l2 != l3 and s == 1:
    print('{}{}'.format(sim, tipo[2]))
if s == 0:
    print('\nNão é possível formar um triângulo!\n')