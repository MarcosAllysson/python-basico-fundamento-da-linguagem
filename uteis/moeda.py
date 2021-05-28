"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


def aumentar(num, porcent=10):
    """
    Função que aumenta num em x %. Caso não for informado, é calculado 10% por padrão.
    :param num: número inteiro
    :return: 13% do num
    """
    porcentagem = num + ((porcent / 100) * num)
    return f'\033[36mAumentando {porcent}% de R$ {num} é R$ {porcentagem:.2f}\033[m'


def diminuir(num, porcent=10):
    """
    Função que diminui num em x %. Caso não for informado, é calculado 10% por padrão.
    :param num: número inteiro
    :return: 13% do num
    """
    porcentagem = num - ((porcent / 100) * num)
    return f'\033[35mDiminuindo {porcent}% de R$ {num} é R$ {porcentagem:.2f}\033[m'


def dobro(num):
    """
    Função que dobro num
    :param num: número inteiro
    :return: dobro de num
    """
    return f'\033[32mO dobro de R$ {num} é R$ {num * 2}\033[m'


def metade(num):
    """
    Função que divide num
    :param num: número inteiro
    :return: metade de num
    """
    return f'\033[34mR$ {num} / 2 = R$ {num / 2}\033[m'
