"""
Faça um programa que leia largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta
necessário para pintá-la. Sabendo que, cada litro de tinta, pinta uma área de 2m**2 (2 metros quadrados).
"""

print('LITROS DE TINTA')
largura = float(input('Qual largura da parede? '))
altura = float(input('Qual altura da parede? '))
area = largura * altura
quantidade = area / 2

print('Como a área vale \033[1;31;40m{}\033[m metros, você precisa de {:.2f} litros de tinta pra pintar a parede.'.format(area, quantidade))
