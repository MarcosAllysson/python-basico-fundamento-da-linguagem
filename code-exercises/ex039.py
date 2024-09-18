"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
from emoji import emojize
print('\033[39mALISTAMENTO MILITAR\033[m')

ano_nascimento = int(input('Qual ano de nascimento? '))
sexo = int(input('Qual seu sexo? \n1 - Masculino; \n2 - Feminino \nDigite opção: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if ano_nascimento > ano_atual:
    print(emojize('Oxê, veio do futuro foi :smile: !?', use_aliases=True))
elif sexo == 2:
    print('Você é mulher, e no Brasil, o alistamento militar é opcional.')
elif idade < 18 and sexo == 1:
    print('Você ainda vai se alistar, faltam apenas {} anos.'.format(18 - idade))
elif idade > 18 and sexo == 1:
    print('Vixe, já passou {} anos do alistamento militar obrigatório!'.format(idade - 18))
else:
    print('Aos 18 anos você está apto ao alistamento militar obrigatório!')
