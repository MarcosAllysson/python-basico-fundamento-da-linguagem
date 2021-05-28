"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente.
Ex: Marcos A Silva
primeiro nome = Marcos
último: Silva
"""

print('PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA')
nome_completo = str(input('Digite seu nome completo: '))
primeiro_nome = nome_completo.strip().split(' ')[0]

#começando da última posição, retorna apenas a primeiro posição no índice.
ultimo_nome = nome_completo.strip().split(' ')[::-1][0]

print('Primeiro nome: \033[1;36m{}\033[m, \núltimo nome: \033[4;41m{}\033[m'.format(primeiro_nome, ultimo_nome))

#outra opção pra printar último nome
#nome_completo[len(nome_completo)-1]