# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante
# o campeonato.

status = {}
lista = []
total = 0
status['Nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {status["Nome"]} jogou? '))
for c in range(0, partidas):
    soma = int(input(f'Quantos gols na partidaf {c}? '))
    lista.append(soma)
    total += soma
status['Gols'] = lista[:]
status['Total'] = total
print('=-='*40)
print(status)
print('=-='*40)
for k, v in status.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-='*40)
print(f'O jogador {status["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(status['Gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {status["Total"]} gols.')
