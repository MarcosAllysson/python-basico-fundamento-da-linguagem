def fatorial(num):
    """
    Função que calcula o fatorial de n
    :param num: número inteiro pra calcular o fatorial
    :return: fatorial de num
    """
    fac = 1
    for i in range(num, 0, -1):
        fac *= i

    return f'O fatorial de {num}, é {fac}.'


def dobro(num):
    """
    Função que calcula o dobro de num
    :param num: número inteiro pra calcular o dobro
    :return: dobro de num
    """
    return f'O triplo de {num}, é {num * 2}.'


def triplo(num):
    """
    Função que calcula o triplo de num
    :param num: número inteiro pra calcular o triplo
    :return: triplo de num
    """
    return f'O triplo de {num}, é {num * 3}.'
