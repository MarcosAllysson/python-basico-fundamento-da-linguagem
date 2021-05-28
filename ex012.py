"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

print('PREÇO COM DESCONTO')
preco = float(input('Informe o preço do produto: '))
calcula_desconto = preco * (5 / 100)
novo_preco = preco - calcula_desconto

print('Valor antigo era de R${}, com 5% de desconto, passa a custar R$ {:.2f}'.format(preco, novo_preco))
