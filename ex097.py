# Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def escreva(entrada):
    linhas = len(entrada) + 4
    print('~' * linhas)
    print(f'{entrada:^{linhas}}')
    print('~' * linhas)


# programa principal
escreva(str(input('Uma palavra  qualquer: ')))