# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada
# jogador.

status = {}
lista = []
jogadores = []
total = 0
while True:
    status['Nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {status["Nome"]} jogou? '))
    for c in range(0, partidas):
        soma = int(input(f'    Quantos gols na partidaf {c}? '))
        lista.append(soma)
        total += soma
    status['Gols'] = lista[:]
    status['Total'] = total
    continuar = str(input('Quer continuar? (S/N): '))
    jogadores.append(status.copy())
    lista.clear()
    total = 0
    if continuar in 'Nn':
        break
print('=-='*35)
print(f'{"Cod.":<6}{"Nome":<17}{"Gols"}{"Total":>30}')
print('-'*70)
for i, posicao in enumerate(jogadores):
    print(f'{i:<6}{posicao["Nome"]:<17}{posicao["Gols"]}', end='')
    print(f'{posicao["Total"]:>26}')
print('=-='*35)
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    print()
    if dados == 999:
        break
    gols2 = jogadores[dados]
    print(f'----Levantamento do jogador {gols2["Nome"]}:')
    for i, d in enumerate(gols2["Gols"]):
        print(f'    No jogo {i} fez {d} gols.')
    print('-'* 70)
print('Fim do programa...')
