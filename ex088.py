"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from time import sleep
from emoji import emojize
from random import randint

print('\033[31mPALPITES PARA A MEGA SENA\033[m \n')

jogos = []
jogo_temporario = []

palpite_quantidade = int(input('\033[36mQuer gerar quantos jogos?\033[m '))
print(f'\n\033[32mGerando {palpite_quantidade} jogos...\033[m')

for i in range(0, palpite_quantidade):
    jogo_temporario = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]

    # printando em ordem crescente
    jogo_temporario.sort()
    print(f'\033[33mJogo {i+1}\033[m: {jogo_temporario}')

    # sleep 1 segundo
    sleep(1)

    # fazendo cópia da lista temporária pra lista geral
    jogos.append(jogo_temporario[:])

    # limpando lista temporária
    jogo_temporario.clear()

print()
print(emojize('Jogos gerados com sucesso. Boa sorte :kissing_heart::wink::sunglasses::boom: ', use_aliases=True))
