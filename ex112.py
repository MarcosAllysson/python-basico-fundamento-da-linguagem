from uteis import dado
from uteis import moeda_2

"""
Dentro do pacote uteis que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), 
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""
print('Entrada de dados monetários\n')

preco = dado.leiaDinheiro('Informe o preço: R$ ')
print(moeda_2.resumo(preco, 35, 22))
