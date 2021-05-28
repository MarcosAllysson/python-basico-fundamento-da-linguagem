"""
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from emoji import emojize
print('JOGO DA ADIVINHAÇÃO')

numero_computador = randint(0, 5)
numero_usuario = int(input('Qual seu número de palpite entre 0 e 5? '))

if numero_computador == numero_usuario:
    print(emojize('Você venceu! :punch: :clap: ', use_aliases=True))
else:
    print(emojize('Palpite errado, o certo seria {}, tenta de novo :exclamation: '.format(numero_computador), use_aliases=True))
