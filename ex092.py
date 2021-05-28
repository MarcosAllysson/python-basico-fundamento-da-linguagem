"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
print('CADASTRO DE TRABALHADOR\n')

trabalhador = {}
trabalhador['nome'] = str(input('Nome do trabalhador: ')).strip().title()
ano_nascimento = int(input(f'Ano de nascimento do {trabalhador["nome"]}: '))
ano_atual = date.today().year
trabalhador['idade'] = ano_atual - ano_nascimento
trabalhador['carteira'] = int(input('Número da carteira de trabalho: '))

if trabalhador['carteira'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))

    # calculando quantos anos faltam pra aposentar. Considerando 55 anos.
    faltam_anos_aposentadoria = 55 - trabalhador['idade']
    trabalhador['ano_aposentadoria'] = trabalhador['idade'] + faltam_anos_aposentadoria

print()
for chave, valor in trabalhador.items():
    print(f'{chave}: {valor}')
