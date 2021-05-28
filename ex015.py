"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print('CARRO ALUGADO')
km_percorridos = float(input('Quantos KM o carrou rodou? '))
qnt_dias = int(input('Quantos dias o carro rodou? '))
preco = (60 * qnt_dias) + (0.15 * km_percorridos)

print('Depois do cálculo, o carro rodou por {} dias {}km, então o valor final é de \033[0;33mR$ {:.2f}\033[m'.format(qnt_dias, km_percorridos, preco))
