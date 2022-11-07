# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de 
# uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
#  de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(60)
altura = float(1.90)
imc = peso / (altura*altura)
frase1 = 'Você está: '
frase2 = ['Abaixo do peso.', 'Peso Ideal.', 'Sobrepeso.', 'Obesidade.', 
        'Obesidade Mórbida.']
print('\nSeu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('{}{}'.format(frase1, frase2[0]))
elif 18.5 <= imc <= 25:
    print('{}{}'.format(frase1, frase2[1]))
elif 25 < imc <= 30:
    print('{}{}'.format(frase1, frase2[2]))
elif 30 < imc <= 40:
    print('{}{}'.format(frase1, frase2[3]))
else:
    print('{}{}'.format(frase1, frase2[4]))
