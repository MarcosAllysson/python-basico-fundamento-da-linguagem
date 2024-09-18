from uteis import moeda_2

"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
print('Formatando Moedas em Python - 2\n')

valor = float(input('Informe um valor: R$ '))
print(moeda_2.aumentar(valor, 10))
print(moeda_2.diminuir(valor, 10))
print(moeda_2.dobro(valor))
print(moeda_2.metade(valor))

"""
print(help(moeda.dobro()))
print(help(moeda.metade()))
print(help(moeda.diminuir()))
print(help(moeda.aumentar()))
"""
