"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date
print('ANO BISSEXTO')

ano = int(input('Digite o ano para descobrir se é bissexto ou 0 para analisar ano atual: '))
if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é bissexto.'.format(ano))
else:
    print('Esse ano {} não é bissexto.'.format(ano))
