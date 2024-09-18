"""
Crie um programa que faça o computador jogar Jokenpô com você.
* PEDRA, PAPEL, TESOURA.
"""
from random import choice
from time import sleep
print('\033[1;36mPEDRA, PAPEL, TESOURAAA\033[m')

computador_opcoes = ['pedra', 'papel', 'tesoura']
jogada_computador = choice(computador_opcoes)
jogada_usuario = int(input('1 - Pedra; \n2 - Papel; \n3 - Tesoura; \nSua jogada: '))

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURAAAAAAAAAAAAAAAA')
sleep(1)

if jogada_usuario == 1 and jogada_computador == 'pedra':
    print('\033[1;33mEmpate.\033[m')
elif jogada_usuario == 2 and jogada_computador == 'papel':
    print('\033[1;33mEmpate.\033[m')
elif jogada_usuario == 3 and jogada_computador == 'tesoura':
    print('\033[1;33mEmpate.\033[m')
elif jogada_usuario == 1 and jogada_computador == 'papel':
    print('Papel ganha de pedra, \033[31mcomputador ganhou!\033[m')
elif jogada_usuario == 1 and jogada_computador == 'tesoura':
    print('Pedra ganha de tesoura. \033[35mUsuário ganhou!\033[m ')
elif jogada_usuario == 2 and jogada_computador == 'pedra':
    print('Papel embrulha pedra, \033[35musuário ganhou!\033[m')
elif jogada_usuario == 2 and jogada_computador == 'tesoura':
    print('Tesoura corta papel, \033[31mcomputador ganhou!\033[m')
elif jogada_usuario == 3 and jogada_computador == 'pedra':
    print('Pedra quebra tesoura, \033[31mcomputador ganhou!\033[m')
elif jogada_usuario == 3 and jogada_computador == 'papel':
    print('Tesoura corta papel, \033[35musuário ganhou.\033[m')
else:
    print('Opção inválida.')

print()
print('-=-'*10)
print('Escolhas: \nComputador jogou: \033[4:0:41m{}\033[m \nUsuário jogou: \033[4:0:41m{}.\033[m'.format(jogada_computador, jogada_usuario))
print('-=-'*10)
