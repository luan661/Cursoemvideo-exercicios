# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número de 0 a 20: '))
while numero > len(extenso):
    numero = int(input('Valor inválido. Digite novamente: '))
print(f'Seu número por extenso é: {extenso[numero].capitalize()}')
