# 107. Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que
# importe esse módulo e use algumas dessas funções.

# 109. Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas vai
# ser ounão formatado pela função moeda(), desenvolvida no desafio 108.


def metade(item, mostrar=False):
    if mostrar:
        return moeda(item)
    a = item / 2
    return a


def dobro(item, mostrar=False):
    if mostrar:
        return moeda(item)
    a = item * 2
    return a


def dez(item, mostrar=False):
    a = item + (item*(10/100))
    if mostrar:
        return moeda(a)
    return a


def treze(item, mostrar=False):
    if mostrar:
        return moeda(item)
    a = item - (item*(13/100))
    return a


# 108. Adapte o código do desafio #107, criando uma função adicional chamada
# moeda() que consiga mostrar os números como um valor monetário formatado.


def moeda(item):
    i = f'{"R$"}{item:.2f}'.replace('.', ',')
    return i


# 110. Adicione o módulo moeda.py criado nos desafios anteriores, uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.


def certo(i1, i2):
    print(f'{i1:<25}{moeda(i2)}')


def resumo(res):
    print('-' * 35)
    print(f'{"resumo do valor".upper():^35}')
    print('-' * 35)
    certo("Preço analisado: ", res)
    certo("Dobro do preço: ", dobro(res))
    certo("Metade do preço: ", metade(res))
    certo("10% de aumento: ", dez(res))
    certo("13% de redução: ", treze(res))
