# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('palmeiras', 'internacional', 'fluminense', 'corinthians',
         'flamengo', 'atleticopr', 'americamg', 'fortaleza', 'atléticomg',
         'são paulo', 'botafogo', 'santos', 'goiás', 'chapecoense',
         'coritiba', 'cuiabá', 'atléticogo', 'ceará', 'avaí', 'juventude')
print(f'O 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time da Chapecoense está na {times.index("chapecoense")+1}° posição.')
