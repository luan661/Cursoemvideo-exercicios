# Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará quando ele disser
# que quer mostrar 0 termos.

primtermo = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
primtermo1 = 1
count = 0
n = 10
stop = False
while stop == False:
    while count <= n:
        count += 1
        primtermo = count * razao
        print(primtermo, end=' ')
        print('-' if count < n else '', end=' ')
        if count == n:
            plus = int(input('\nQuer mais quantos valores? [Digite 0 para parar.]: '))
            n = n + plus
            if plus == 0:
                stop = True
                count = n+1
print('\nProcesso finalizado.')