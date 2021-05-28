"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
print('\033[36mMAIOR E MENOR VALORES EM TUPLA\033[m \n')

numeros_aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = 0

for i in range(0, 5):
    if i == 0:
        maior = menor = numeros_aleatorios[i]

    else:
        if numeros_aleatorios[i] > maior:
            maior = numeros_aleatorios[i]
        if numeros_aleatorios[i] < menor:
            menor = numeros_aleatorios[i]

print(f'Tupla é formada pelos números: \033[4m{numeros_aleatorios}\033[m.')
print(f'\033[34mMaior número\033[m: \033[4m{maior}\033[m, e o \033[31mmenor\033[m: \033[4m{menor}\033[m.')

#outra solução, usar max() e min()
