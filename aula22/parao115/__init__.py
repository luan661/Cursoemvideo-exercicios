from time import sleep

# Cores pros comandos
def co(d):
    c = [0, 1, 2, 'b', 4]
    c[0] = '\033[m'    # Stopcolor
    c[1] = '\033[32m'  # Verde
    c[2] = '\033[34m'  # Azul
    c[3] = '\033[1m'   # BoldText
    c[4] = '\033[31m'  # Vermelho
    if c[d] in c:
        return c[d]


# Título centralizado
def titulo(strr):
    print('-' * 45)
    print(f'{co(3)}{strr:^45}{co(0)}')
    print('-' * 45)


# Menú do programa
def corpo():
    print(f'{co(1)}1 -{co(0)} {co(2)}Ver pessoas cadastradas{co(0)}')
    print(f'{co(1)}2 -{co(0)} {co(2)}Cadastrar nova Pessoa{co(0)}')
    print(f'{co(1)}3 -{co(0)} {co(2)}Sair do Sistema{co(0)}')
    print('-' * 45)

# Opção 1
def mostrar1():
    return f'{titulo("< PESSOAS CADASTRADAS >")}'


def opcao1():
    mostrar1()
    print(f'{"NOME.":<39}{"IDADE."}')
    print('-' * 45)
    fil = open('pessoas.txt', mode='r', encoding="utf-8")
    for linh in fil:
        print(linh, end='')
    fil.close()
    menu()


# Opção 2
def mostrar2():
    titulo('< CADASTRAR NOVA PESSOA >')


def opcao2():
    mostrar2()
    fil = open('pessoas.txt', mode='a', encoding="utf-8")
    item = input('Nome a ser cadastrado: ').capitalize()
    item2 = input('Idade da pessoa: ')
    fil.write(f'{item:<41}{item2}\n')
    fil.close()
    sleep(0.8)
    print(f'{co(1)}{"CADASTRADO COM SUCESSO!":^45}{co(0)}')
    sleep(0.8)
    menu()


# Leitura das opções
def escolha():
    sim = int()
    continuar = True
    while continuar:
        try:
            i1 = int(input(f'{co(1)}Sua Opção: {co(0)}'))
        except ValueError:
            print(f'{co(4)}ERRO: Por favor digite um número inteiro'
                  f' válido.{co(0)}')
            continue
        else:
            while True:
                if i1 == 1:
                    sleep(0.5)
                    return opcao1()
                elif i1 == 2:
                    sleep(0.5)
                    return opcao2()
                elif i1 == 3:
                    print('-' * 45)
                    break
                else:
                    print(f'{co(4)}Por favor digite uma opção válida!{co(0)}')
                    continue
            break
    print('Terminando programa', end='')
    sleep(0.7)
    print('.', end='', flush=False)
    sleep(0.7)
    print('.', end='', flush=False)
    sleep(0.7)
    print('.', end='\n', flush=False)
    print(f'{co(2)}{co(3)}VOLTE SEMPRE!{co(0)}')


# O programa e estrutura
def menu():
    sleep(0.5)
    titulo('MENU PRINCIPAL')
    corpo()
    escolha()
