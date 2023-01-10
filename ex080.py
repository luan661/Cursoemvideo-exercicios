# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.
#
# RESOLUÇÃO GUANABARA #

lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        n = lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        p = 0
        while p < len(lista):
            if n < lista[p]:
                lista.insert(p, n)
                break
            p += 1
print(lista)
