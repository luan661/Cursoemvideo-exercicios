# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.

print('\nTabuada 2.0\n')
n = int(3)
for c in range(1, 11):
    print('{} X {:>2} == {}'.format(n, c, n * c))
print('\n')
