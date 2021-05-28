"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
"""

print('NÚMERO EM METROS')
numero_em_metros = float(input('Digite um valor: '))
kilometro = numero_em_metros / 1000
hectometro = numero_em_metros / 100
decametro = numero_em_metros / 10
decimetro = numero_em_metros * 10
centimetro = numero_em_metros * 100
milimetro = numero_em_metros * 1000

print('{} metros, convertendo fica {} decímetros, {} centímetros, {} milímetros,'.format(numero_em_metros, decimetro, centimetro, milimetro), end = ' ')
print('{} decametro, {} hectometros e {} kilometros. '.format(decametro, hectometro, kilometro))
