"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""
from time import sleep
print('FUNÇÃO QUE CALCULA ÁREA\n')

def area(largura, comprimento):
    area = largura * comprimento
    print(f'Área recebida: {largura} x {comprimento}, a aŕea do terreno vale: {area:.2f}m2.')


# main
print('Calcula área: ')
largura = float(input('Qual tamanho da área? '))
comprimento = float(input('E do comprimento? '))
print('Ok, vamos lá...')
sleep(2)

# chamando função, passando parâmetros pro cálculo da área.
area(largura, comprimento)
