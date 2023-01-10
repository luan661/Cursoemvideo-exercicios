# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário
# vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
# palavra 'FIM', o programa se encerrará. Importante: use cores.


def inicio(mensagem):
    while True:
        print('\033[42m~'*(len(mensagem)+2))
        print(f'{mensagem:^{(len(mensagem)+2)}}')
        print('~' * (len(mensagem) + 2))
        print('\033[m', end='')
        fb = input('Função ou Biblioteca > ')
        acess = f'Acessando o manual do comando "{fb}".'.lower()
        if fb == 'fim':
            break
        else:
            print('\033[44m~' * (len(acess) + 2))
            print(f'{acess:^{(len(acess) + 2)}}')
            print('~' * (len(acess) + 2))
            print('\033[m', end='')
            print()
            print('\033[7m')
            print(f'{help(fb)}')
            print('\033[m')


prog = inicio('SISTEMA DE AJUDA PyHELP')
atelogo = 'ATÉ LOGO!'
print('\033[41m~'*(len(atelogo)+2))
print(f'{atelogo:^{(len(atelogo)+2)}}')
print('~' * (len(atelogo) + 2))
print('\033[m', end='')
