# Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo da
# estrutura na tela.

aluno = {}
lista = []
aluno['Nome'] = str(input('Nome: ').capitalize())
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação'] = ''
lista.append(aluno.copy())
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
    if v == aluno["Média"]:
        if v < 6:
            aluno['Situação'] = 'REPROVADO!'
        else:
            aluno['Situação'] = 'APROVADO!'
