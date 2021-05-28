"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('\033[1;36mJOGO DO PAR OU ÍMPAR\033[m')
vitorias_consecutivas = 0

while True:
    numero_computador = randint(0, 10)
    numero_usuario = int(input('\033[33mEscolha seu número\033[m: '))
    escolha_usuario = str(input('\033[4mPar ou ímpar\033[m? [Par/Impar]: ')).strip().upper()[0]

    # verificando se o usuário realmente digitou 'par' ou 'impar', analisando 1° caractere.
    #while escolha_usuario not in 'PI':
    while escolha_usuario != 'P' and escolha_usuario != 'I':
        escolha_usuario = str(input('\033[4mPar ou ímpar\033[m? [Par/Impar]: ')).strip().upper()[0]

    # verificando se a soma dos números é par
    if (numero_computador + numero_usuario) % 2 == 0:
        print(f'{numero_computador} + {numero_usuario} = {numero_computador + numero_usuario}. \033[31mDeu Par!\033[m')

        # verificando se o usuário escolheu Pai, se sim, ele ganha. Se não, computador ganha.
        if escolha_usuario == 'P':
            print('\033[36mEu ganhei.\033[m')
            vitorias_consecutivas += 1
        else:
            print('\033[35mComputador ganhou\033[m.')
            break

    # se não for par, é ímpar
    else:
        print(f'{numero_computador} + {numero_usuario} = {numero_computador + numero_usuario}. \033[31mDeu Ímpar!\033[m')

        # verificando se o usuário escolheu Ímpar, se sim, ele ganha. Se não, computador ganha.
        if escolha_usuario == 'I':
            print('\033[36mEu ganhei\033[m.')
            vitorias_consecutivas += 1

        else:
            print('\033[35mComputador ganhou\033[m.')
            break

    # jogador ganhou, começa de novo...
    print('Simbora de novo =D! ')

print(f'\033[1;34;40mEu ganhei\033[m: {vitorias_consecutivas}x seguidas.')
