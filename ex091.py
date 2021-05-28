"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter  # ordenar dicionário

print('JOGO DE DADOS EM PYTHON\n')

jogadores = dict()
print(f'{" Sorteando números dos jogadores... ":=^30}\n')
sleep(1)

jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

print(f'{" Valores sorteados: ":=^30} ')
for chave, valor in jogadores.items():
    print(f'O {chave} tirou o número {valor}.')
    sleep(1)

# lista do ranking
ranking = []

# ordendo dicionário. Itemgetter 0, ordem de chaves. Itemgetter 1, ordem de valores. Como no exercício.
# como retorna em ordem crescente, basta usar reverse=True pra printar em decrescente.
# retorna uma lista com tuplas
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(f'\n{" GERANDO RANKING ":=^30}')
sleep(1)
for chave, valor in enumerate(ranking):
    # Printando a tupla ...
    print(f'{chave + 1}° lugar: {valor[0]}, com {valor[1]} pontos.')
    sleep(1)
