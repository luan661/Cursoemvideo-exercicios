# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
# a possibilidade da digitação de um número de tipo inválido. Aproveite e
# crie também uma função leiaFloat() com a mesma funcionalidade.
#
#### RESOLUÇÃO GUANABARA ###

def leiaint(frase):
    sim = True
    while sim:
        try:
            a = int(input(frase))
        except:
            print('\033[31mERRO: Por favor digite um número inteiro válido.'
                  '\033[m')
            continue
        else:
            sim = False
            return a


def leiafloat(numero):
    sim = True
    while sim:
        try:
            a = float(input(numero))
        except:
            print(f'\033[31mPor favor digite um número real válido.\033[m')
            continue
        else:
            sim = False
            return a


n = leiaint('Digite o valor inteiro: ')
n2 = leiafloat('Digite o valor real: ')
print(f'Você digitou o valor inteiro {n} e o valor real {n2}')
