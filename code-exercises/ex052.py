"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print('Números primos'.upper())

numero = int(input('\033[4mDigite o número:\033[m'))
cont = 0

for i in range(1, numero+1):
    if numero % i == 0:
        cont += 1

if cont == 2:
    print('\033[36m{}\033[m \033[4mé primo.\033[m'.format(numero))
else:
    print('\033[36m{}\033[m \033[4mnão é primo.\033[m'.format(numero))
