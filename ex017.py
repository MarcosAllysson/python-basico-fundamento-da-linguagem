"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.
"""
# pra calcular hipotenusa
from math import hypot

print('CATETOS E HIPOTENUSA')
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjavente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# outra forma de calcular via fórmula matemática
fórmula_hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('Comprimento da hipotenusa é \033[4m{:.2f}.\033[m'.format(hipotenusa))
print('Via fórmula matemática, {:.2f}.'.format(fórmula_hipotenusa))
