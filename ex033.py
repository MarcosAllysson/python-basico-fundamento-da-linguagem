"""
Faça um programa que leia 3 números e mostre qual é o maior e o menor.
"""
print('MAIOR E MENOR VALORES')

num1 = int(input('Digite primeiro número: '))
num2 = int(input('Digite segundo número: '))
num3 = int(input('Digite terceiro número: '))

print('Maior valor digitado {}'.format(max(num1, num2, num3)), ', e o menor {}.'.format(min(num1, num2, num3)))
