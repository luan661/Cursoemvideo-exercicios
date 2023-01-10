# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
# módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
# capaz de funcionar como a função input(), mas com uma validação de
# dados para aceitar apenas valores que seja monetários.


from aula22.parao112.dados import dado
from aula22 import moeda

rs = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(rs)
