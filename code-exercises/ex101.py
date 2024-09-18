"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from datetime import date

print('FUNÇÕES PARA VOTAÇÕES\n')


def vota(nascimento):
    """
    Função que recebe ano de nascimento, e retorna a situação da pessoa em relação a obrigatoriedade do voto.
    :param nascimento: número inteiro do nascimento do usuário
    :return: se < 18, NEGADO, se > 65, OPCIONAL, senão, OBRIGATÓRIO.
    """
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    if idade < 18:
        return f'Com {idade} anos \033[31mNÃO VOTA\033[m.'
    elif idade < 65:
        return f'Com {idade} anos, voto é \033[31mOBRIGATÓRIO\033[m.'
    else:
        return f'Com {idade} anos, voto é \033[31mOPCIONAL\033[m.'


nascimento = int(input('Em que ano nasceu? '))
print(vota(nascimento))
# help(vota)
