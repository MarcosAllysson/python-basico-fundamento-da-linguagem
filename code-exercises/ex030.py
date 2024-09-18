"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
"""
print('PAR OU ÍMPAR?')

numero = int(input('Qual número? '))
print('Número é par!' if numero % 2 == 0 else 'Número é ímpar.')
