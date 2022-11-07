# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por 
# cada Km acima do limite.

velocidade_do_carro = int(input('Velocidade do carro no momento = '))
if velocidade_do_carro < 80:
    print('Tenha um bom dia. Dirija com segurança!')
else:
    print('Você foi multado!\nValor da multa R$: {}'.format(
        int(velocidade_do_carro - 79) * 7) 
    )