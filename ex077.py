# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos).Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.
#
# RESOLUÇÃO GUANABARA #
#

palavras = ('acucar', 'arroz', 'biscoitos', 'cafe', 'carnes', 'farinha',
            'feijao', 'fermento', 'hortalicas', 'iogurte', 'leite',
            'macarrao', 'margarina', 'molho de tomate', 'oleo', 'ovos',
            'paes', 'queijo ralado', 'sal', 'temperos', 'agua sanitaria',
            'alcool em gel', 'amaciante', 'desinfetante', 'detergente',
            'esponja de aco', 'esponja de pia', 'flanelas')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')
