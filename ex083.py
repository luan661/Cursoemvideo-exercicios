# Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.
#
# RESOLUÇÃO GUANABARA #

# n = input('Digite uma expressão: ')
# contador1 = n.count('(')
# contador2 = n.count(')')
# if contador1 != contador2:
#     print('Erro na expressão.')
# else:
#     print('Expressão válida.')

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if pilha == 0:
    print('Solução válida.')
else:
    print('Solução inválida.')