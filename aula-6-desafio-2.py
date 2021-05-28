"""
Faça um programa que leia algo pelo teclado o seu tipo primitivo e todas as informações
possíveis sobre ela usando os vários .is...()
"""

print('=== Desafio 2 ===')
algoNaTela = input('Digite algo: ')
tipoPrimitivo = type(algoNaTela)
print('Tipo primitivo: ', tipoPrimitivo)
print('É número? ', algoNaTela.isdigit())
print('É alfa numérico?', algoNaTela.isalnum())
print('É letra?', algoNaTela.isalpha())
print('Ascii: ', algoNaTela.isascii())
print('É tudo minúsculo? ', algoNaTela.islower())
print('É decimal?', algoNaTela.isdecimal())
print('Id: ', algoNaTela.isidentifier())
print('É número?', algoNaTela.isnumeric())
print('Pode printar?', algoNaTela.isprintable())
print('É um espaço em branco?', algoNaTela.isspace())
print('É um título?', algoNaTela.istitle())
print('É tudo maisuscúlo?', algoNaTela.isupper())
