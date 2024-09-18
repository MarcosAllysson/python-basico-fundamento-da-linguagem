"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
from time import sleep

print('APRIMORANDO OS DICIONÁRIOS\n')

jogador = {}
lista_jogadores = []
cont = 1
contador = 1
gols_por_partida = []
total_gols = 0

while True:
    jogador['nome'] = str(input('\033[32mNome do jogador\033[m: ')).strip().title()
    jogador['qnt_partidas'] = int(input(f'\033[32mQuantas partidas {jogador["nome"]} jogou?\033[m '))

    # anotando gols por partida e somando total de gols
    while cont <= jogador['qnt_partidas']:
        gols = int(input(f'\033[32mQuantos gols na {cont}° partida?\033[m '))
        gols_por_partida.append(gols)
        cont += 1
        total_gols += gols

    # adicionando a lista com quantidade de gols por partida no dicionário
    jogador['gol_por_partida'] = gols_por_partida[:]
    jogador['total_de_gols'] = total_gols

    # cópia do dicionário pra lista
    lista_jogadores.append(jogador.copy())

    # zerando contador
    cont = 1

    # limpando lista
    jogador.clear()
    gols_por_partida.clear()
    total_gols = 0

    while True:
        escolha = str(input('\nQuer adicionar outro jogador (Sim/Não)? ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Digite somente Sim (S) ou Não (N)! ')

    if escolha == 'N':
        break

# cabeçalho
"""print('cod ', end='')
for i in lista_jogadores[0].keys():
    print(f'{i:<15}', end='')
print()"""

# dados gerais
print('\nDADOS GERAIS')
print('cod {:>5} {:>15} {:>13} {:>14}'.format('nome', 'partidas', 'gols', 'total'))

for chave, valor in enumerate(lista_jogadores):
    print(f'{chave:>4} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()

print('\n')
while True:
    opcao_jogador = int(input('\nQuer ver os dados de qual jogador? \n(999 para parar)! \nSua escolha: '))
    if opcao_jogador == 999:
        break

    if opcao_jogador >= len(lista_jogadores):
        print(f'Jogador não encontrado ou fora da faixa...\nTem {len(lista_jogadores)} jogadores cadastrados.')

    else:
        print(f'\033[31m\nOk, Gerando Relatório do {lista_jogadores[opcao_jogador]["nome"]}...\033[m ')
        sleep(2)

        # gerando dados
        print(f'Ele jogou {lista_jogadores[opcao_jogador]["qnt_partidas"]} partidas:')

        for chave, valor in enumerate(lista_jogadores[opcao_jogador]['gol_por_partida']):
            print(f'-> Na {chave+1}° partida, fez {valor} gols.')

        print(f'No total, fez {lista_jogadores[opcao_jogador]["total_de_gols"]} gols no campeonato.')
