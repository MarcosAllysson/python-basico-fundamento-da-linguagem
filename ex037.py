"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
print('\033[1;31mCONVERSOR DE BASES NUMÉRICAS\033[m')
numero = int(input('Insira um número qualquer: '))
base_conversao = int(input('Qual base de conversão? \n1 - Binário; \n2 - Octal; \n3 - Hexadecimal. \nSua opção: '))

if base_conversao == 1:
    print('Número inserido: {}, convertido para binário: {}.'.format(numero, bin(numero)[2:]))
elif base_conversao == 2:
    print('Número inserido: {}, convertido para octal: {}.'.format(numero, oct(numero)[2:]))
elif base_conversao == 3:
    print('Número inserido: {}, convertido para hexadecimal: {}.'.format(numero, hex(numero)[2:]))
else:
    print('Nenhuma opção escolhida. Tente novamente!')
