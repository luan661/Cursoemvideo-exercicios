# Escreva um programa que pergunte o salário de um funcionário e calcule o valor 
# do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 
# 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Aumento de salário. Quanto vc recebe?: '))
if salário <= 1250:
    salario_aumento = salário * (15/100) + salário
    print('Aumento de 15% para rendas abaixo de R$1250 ou igual: R${:.2f}'.format(salario_aumento))
if salário > 1250:
    salario_aumento2 = salário * (10/100) + salário
    print('Aumento de 10 % para salários superiores a R$1250: R${:.2f}'.format(salario_aumento2))
 