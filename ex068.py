# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

c = 0
while True:
    computer = randint(1, 10)
    v = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar?[P/I]: '))
    resultado = computer + v
    veredito, pi1, ganhou = (f'Você jogou {v} e o computador {computer}. '
              f'Total de {resultado} deu'), str(), ('\nVocê venceu! Vamos jogar '
              f'novamente...')
    if resultado % 2 == 0 and pi in 'Pp':
        pi1 = 'PAR.'
        c = c+1
        print(veredito, pi1, ganhou)
    elif resultado % 2 != 0 and pi in 'Ii':
        pi1 = 'ÍMPAR.'
        c = c+1
        print(veredito, pi1, ganhou)
    else:
        if resultado % 2 == 0:
            print(veredito, 'PAR')
        elif resultado % 2 != 0:
            print(veredito, 'ÍMPAR')
        print('Você perdeu!')
        print(f'Você venceu {c} vezes.')
        break
