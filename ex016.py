"""
Crie um programa que leia um número qualquer no teclado e mostre na tela a sua porção inteira.
Ex: número 6.127, o número 6.127 tem a parte inteira 6
"""

# Importando apenas módulo floor (pega inteiro), da biblioteca math
from math import floor

# também pode ser resolvido com trunc
from math import trunc

print('QUEBRANDO UM NÚMERO')
num = float(input('Digite um número qualquer: '))
inteiro_floor = floor(num)
inteiro_trunc = trunc(num)
inteiro_int = int(num)
print('O número {} tem a parte inteira {}.'.format(num, inteiro_floor))
print('O número {} tem a parte inteira {}.'.format(num, inteiro_trunc))
print('O número {} tem a parte inteira {}.'.format(num, inteiro_int))
