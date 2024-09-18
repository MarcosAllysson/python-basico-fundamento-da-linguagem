"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep
print('FUNÇÕES PARA SORTEAR E SOMAR\n')


def sorteia():
    numeros = []
    print('Gerando 5 valores e adicionando à lista... \n')

    for i in range(1, 6):
        print(f'Gerando {i}° valor...')
        sleep(0.7)
        numeros.append(randint(1, 10))

    print('\nNúmeros gerados: ')
    for i in numeros:
        print(i, end=' ')

    print('\nVamos somar os pares agora... ')
    # chamando função somaPar, passando como parâmetro a lista dos números aleatórios gerados.
    sleep(2)
    somaPar(numeros)


def somaPar(lista):
    soma_par = 0
    pares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
            soma_par += numero

    print(f'Soma dos valores pares {pares}, vale {soma_par}.')


# chamando função
sorteia()
