"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
print('TUPLAS COM TIMES DE FUTEBOL')

tabela_brasileirao = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia',
                                'Bragantino', 'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo',
                                'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude',
                                'Palmeiras', 'Santos', 'São Paulo', 'Sport')

print('Os 5 primeiros times: ')
for i in range(0, 5):
    print(f'{i+1}° colocado: \033[31m{tabela_brasileirao[i]}\033[m. ')
# outra solução: print(tabela_brasileirao[:5])

print()
ultimos4 = len(tabela_brasileirao)-4
print('Últimos 4 colocados: \n', tabela_brasileirao[ultimos4:])
# outra solução: print(f'Últimos 4: {tabela_brasileirao[-4:]} ')

print('\nTimes em ordem alfabética: ')
tabela_brasileirao_ordem = sorted(tabela_brasileirao)
qnt = len(tabela_brasileirao_ordem)
for i in range(0, qnt):
    print(f'{i+1}° colocado: ', tabela_brasileirao[i])

#Em que posição está o time da Chapecoense.
print()
if 'Chapecoense' in tabela_brasileirao:
    print('Chapecoense tá na {}° posição.'.format(tabela_brasileirao.index('Chapecoense')+1))
else:
    print('Chape não tá jogando esse ano...')
