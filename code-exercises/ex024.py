"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou com o nome 'SANTO'
"""

print('VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO')
cidade = str(input('Qual nome da cidade: '))
comeca_com_santo = cidade.strip().split(' ')[0]

print('A cidade {}, começa com "SANTO"? -> '.format(cidade), 'SANTO' in comeca_com_santo.upper())

#outra opção é tirar os espaços da esquerda com lstrip, e fatiar assim: [cidade:5], ou seja, 5 primeiros índices.
