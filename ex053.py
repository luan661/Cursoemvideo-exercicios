# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

a = str(input('\nDigite uma palavra e verifique se ela'
        ' é palíndroma: ')).strip().replace(' ', '').upper()
b = len(a)
d = str()
for c in range(b, 0, -1):
    c = (a[(-c)])
    d = c + d
print('Palavra normal: {}, n° de letras({})'
    '\nPalavra ao contrário: {}, n° de letras({})'.format
    (a, len(a), d, len(d)))
if d == a:
    print('\033[33mÉ uma palavra palíndroma.\033[m\n')
else:
    print('\033[31mNão é uma palavra palíndroma.\033[m\n')
