"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
"""

print('PROCURANDO UMA STRING DENTRO DE OUTRA')

nome = str(input('Nome da pessoa: '))
print('O nome \033[1;36m{}\033[m, tem "SILVA"? -> '.format(nome), 'SILVA' in nome.upper())
