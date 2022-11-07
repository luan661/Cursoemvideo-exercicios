# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

termospa = int(input('Digite um número para sua PA: '))
passos = int(input('De quanto em quanto? '))
pa = (termospa + (10-1) * passos)+passos
termospa1 = termospa
while pa > termospa:
    pa = pa - passos
    print('{}'.format(termospa1), end='')
    print(' = ' if pa > termospa else '', end='')
    termospa1 = termospa1 + passos
