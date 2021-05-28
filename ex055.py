"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
print('MAIOR E MENOR DA SEQUÊNCIA')

lista_peso = []
for i in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(i)))
    lista_peso.append(peso)

print('Maior: {}Kg, menor: {}Kg.'.format(max(lista_peso), min(lista_peso)))
