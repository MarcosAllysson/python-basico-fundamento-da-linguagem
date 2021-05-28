"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
from datetime import date

print('CLASSIFICANDO ATLETAS')
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if ano_nascimento > ano_atual:
    print('Oxê, veio do futuro foi!? Kkkkkkk.')
elif idade <= 9:
    print('Como você tem {} anos, até 9 anos, sua categoria é MIRIM.'.format(idade))
elif idade <= 14:
    print('Como você tem {} anos, até 14 anos, sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('Como você tem {} anos, até 19 anos, sua categoria é JÚNIOR.'.format(idade))
elif idade <= 25:
    print('Como você tem {} anos, até 25 anos, sua categoria é SÊNIOR.'.format(idade))
else:
    print('Como você tem {} anos, acima de 25 anos, sua categoria é MASTER.'.format(idade))
