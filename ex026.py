# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
# aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

letraa = str(input('Digite um texto para indentificar "A": ')).lower().strip()
print(letraa.count('a'))
print('A primeira letra "A" fica na posição {} e a segunda na posição {}'.format
((letraa.find('a')), (letraa.rfind('a'))))
