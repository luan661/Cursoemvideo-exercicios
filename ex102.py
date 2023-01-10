# Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e outro chamado
# show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: Mostra ou não a conta.
    :return: O valor do fatorial de N.
    """
    f = 1
    print('-' * 35)
    if show == True:
        for c in range(n, 0, -1):
            print(c, end=' x ' if c > 1 else ' = ')
            f *= c
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f


print(fatorial(5, show=True))