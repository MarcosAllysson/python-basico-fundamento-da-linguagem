"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere = US$ = 1,00 = R$ 3,27
"""

print('DÓLARES NA CARTEIRA')
valor = float(input('Quanto você tem na carteira? R$ '))
if valor < 5.27:
    print('Você não pode comprar nenhum dólar, por que 1 dólar custa R$ 5,27.')
if valor < 6.40:
    print('Você não pode comprar euro, por que hoje custa R$ 6,40.')
else:
    dolares = valor / 5.27
    euro = valor / 6.40
    print('Com R$ {}, você consegue comprar U${:.2f} e E{:.2f}.'.format(valor, dolares, euro))
