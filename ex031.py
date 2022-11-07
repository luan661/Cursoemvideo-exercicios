# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 
# 200Km e R$0,45 parta viagens mais longas.

distancia_da_viagem = int(input('Qual a distância da viagem? R$'))
if distancia_da_viagem < 200:
    print('Tragentória de {} km. Preço da viagem R$: {}'.format
    (distancia_da_viagem, distancia_da_viagem * 0.50))
else:
    print(
        'Tragetória de {} KM. Preço da viagem R$: {}'.format
        (distancia_da_viagem, distancia_da_viagem * 0.45)
    )