# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante a função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


def leiaint(a):
    num = input(a)
    while True:
        while num.isnumeric() == False:
            print('\033[31mERROR! Digite um número inteiro válido.\033[m')
            num = input(a)
        break
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')