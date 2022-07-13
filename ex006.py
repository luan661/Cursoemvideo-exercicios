#crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raíz quadrada

a = float(input('digite um numero: '))
d = a*2
t = a*3
r = a**(1/2)
print('o número: {}\nseu dobro: {}\nseu triplo: {}\nsua raíz quadrada: {:.1f}'.format(a, d, t, r))


