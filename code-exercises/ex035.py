"""
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('ANALISANDO TRIÂNGULO')

reta1 = float(input('Comprimento da reta 1: '))
reta2 = float(input('Comprimento da reta 2: '))
reta3 = float(input('Comprimento da reta 3: '))

# Se a soma de dois lados quaisquer for maior que o terceiro lado é triângulo
if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta3 + reta1 > reta2):
    print('É um triângulo, pois a soma de qualquer dos lados é maior que o 3° comprimento. ')
else:
    print('Não tem como formar triângulo, pois a soma de um dos lados não é maior que o 3° comprimento.')
