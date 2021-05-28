"""
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão aritmética usando a estrutura while
"""
print('PROGRESSÃO ARITMÉTICA 2.0')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
