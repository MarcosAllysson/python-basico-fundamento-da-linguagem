"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequência fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""

print('SEQUÊNCIA DE FIBONACCI')

termos = int(input('Quer mostrar quantos termos? '))
termo1 = 0
termo2 = 1

print('{} -> {}'.format(termo1, termo2), end='')

cont = 3
while cont <= termos:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')

    # passando / transferindo os valores.
    termo1 = termo2
    termo2 = termo3
    cont += 1
