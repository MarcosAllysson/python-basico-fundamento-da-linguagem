"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep
print('FUNÇÃO DE CONTADOR\n')


def contador(inicio, fim, passos):
    print(f'\nDe {inicio} a {fim} de {passos} em {passos}:')

    if passos == 0:
        passos = 1
        for i in range(inicio, fim - 1, passos):
            print(f'{i}', end=' ')
            sleep(0.5)

    if inicio >= fim:
        passos *= -1
        for i in range(inicio, fim - 1, passos):
            print(f'{i}', end=' ')
            sleep(0.5)

    if passos < 0:
        passos *= -1
        for i in range(inicio, fim, passos):
            print(f'{i}', end=' ')
            sleep(0.5)

    else:
        for i in range(inicio, fim + 1, passos):
            print(f'{i}', end=' ')
            sleep(0.5)


print('De 1 a 10 de 1 em 1:')
for i in range(1, 11):
    print(f'{i}', end=' ')
    sleep(0.5)
print()  # quebrando linha

print('\nDe 10 a 0 de 2 em 2:')
for i in range(10, 0, -2):
    print(f'{i}', end=' ')
    sleep(0.5)
print()  # quebrando linha


print('\nAgora é sua vez: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passos = int(input('Passos: '))


# chamada da função:
contador(inicio, fim, passos)
