# Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(* num, sit=False):
    """
    notas(*n, sit=False)
    -> Função para analizar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos.
    :param sit: valor opcional para indicar se deve ou não mostrar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    alunos = {"Total": len(num)}
    maxim = minim = media = 0
    for c in num:
        media += c
        if c == num[0]:
            maxim = minim = c
        else:
            if c > maxim:
                maxim = c
            if c < minim:
                minim = c
    alunos["Maior"] = maxim
    alunos["Menor"] = minim
    alunos["Média"] = media / len(num)
    if sit:
        if alunos["Média"] > 7:
            alunos["Situação"] = 'BOA'
        elif 5 < alunos["Média"] < 7:
            alunos["Situação"] = 'RAZOÁVEL'
        else:
            alunos["Situação"] = 'RUIM'
    return alunos


# programa principal
resp = notas(9, 3, 9, 9.5, 10, 6.5, sit=True)
print(resp)
