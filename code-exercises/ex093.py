"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
from time import sleep
print('\033[36mCADASTRO DE TRABALHADOR DE FUTEBOL\033[m\n')

jogador = {}
cont = 1
contador = 1
gols_por_partida = []
total_gols = 0

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
# outra opção de somar: sum(gols_por_partida) - usando próprio método de somar índices da lista do python


# imprimindo dados
print(f'\033[31m\nOk, Gerando Relatório do {jogador["nome"]}...\033[m ')
sleep(2)


# primeira opção - mais simples:
print('\n\033[1;33mExibindo de forma simples:\033[m ')
print('='*45)
print(jogador)
print('='*45)


# segunda opção
sleep(2)
print('\n\033[1;33mExibindo de forma mais apresentável:\033[m ')
print('*'*45)
for chave, valor in jogador.items():
    print(f'\033[36m{chave}\033[m: \033[34m{valor}\033[m')
print('*'*45)


# terceira opção
sleep(2)
print('-='*25)
print('\n\033[1;33mForma mais detalhada:\033[m ')
print(f'O {jogador["nome"]} jogou {jogador["qnt_partidas"]} partidas:')

while contador <= jogador['qnt_partidas']:
    print(f' -> Na {contador}° partida, fez {jogador["gol_por_partida"][contador-1]} gols...')
    contador += 1

print(f'No total, fez {jogador["total_de_gols"]} gols no campeonato.')
print('-='*25)
