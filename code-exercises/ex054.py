"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
print('Grupo da Maioridade'.upper())
ano_atual = date.today().year
cont_nao_maioridade = 0
cont_maioridade = 0

"""
Outras verificações:
- se tem 4 dígitos
- se é menor que o ano atual
- tratar erro caso não digite número
- plural de 'pessoas', caso existe apenas 1.
"""

for i in range(1, 8):
    ano_nascimento = int(input('Ano de nascimento da {}° pessoa: '.format(i)))

    # se a idade for menor que 21, ainda não atingiu a maioridade.
    if ano_atual - ano_nascimento < 21:
        cont_nao_maioridade += 1

    # sendo maior ou igual a 21, já atingiu maioridade.
    else:
        cont_maioridade += 1

print('{} pessoas ainda não atingiram a maioridade. Apenas {} já são maiores.'.format(cont_nao_maioridade, cont_maioridade))

