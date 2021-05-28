"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""
from math import factorial

print('CÁLCULO DO FATORIAL')

# SOLUÇÃO COM WHILE
numero = int(input('Digite valor pra calcular fatorial: '))
cont = numero
fator_nulo = 1

print('Calculando {}! = '.format(numero), end='')

while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fator_nulo *= cont
    cont -= 1
print('{}.'.format(fator_nulo))


# SOLUÇÃO COM FOR
for i in range(cont, fator_nulo, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fator_nulo *= cont
    cont -= 1
print('Com FOR: {}.'.format(fator_nulo))


# opção 3: com factorial do módulo math do próprio Python
print('Com módulo factorial do math: {} '.format(factorial(numero)))
