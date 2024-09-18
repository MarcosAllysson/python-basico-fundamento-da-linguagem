"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
from emoji import emojize

print('\033[36mCONTAGEM REGRESSIVA\033[m')
for i in range(10, 0-1, -1):
    print(i)
    sleep(1)
print(emojize(':tada: :tada: :rocket: :rocket: :fireworks: :fireworks: ', use_aliases=True))
