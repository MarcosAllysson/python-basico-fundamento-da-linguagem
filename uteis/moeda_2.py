"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""


def aumentar(num, porcent=10):
    """
    Função que aumenta num em x %. Caso não for informado, é calculado 10% por padrão.
    :param num: número inteiro
    :return: 13% do num
    """
    porcentagem = num + ((porcent / 100) * num)
    return f'\033[36mAumentando {porcent}% de {moeda(num)} é {moeda(porcentagem)}\033[m'


def diminuir(num, porcent=10):
    """
    Função que diminui num em x %. Caso não for informado, é calculado 10% por padrão.
    :param num: número inteiro
    :return: 13% do num
    """
    porcentagem = num - ((porcent / 100) * num)
    return f'\033[35mDiminuindo {porcent}% de {moeda(num)} é {moeda(porcentagem)}\033[m'


def dobro(num):
    """
    Função que dobro num
    :param num: número inteiro
    :return: dobro de num
    """
    dobro = num * 2
    return f'\033[32mO dobro de {moeda(num)} é {moeda(dobro)}\033[m'


def metade(num):
    """
    Função que divide num
    :param num: número inteiro
    :return: metade de num
    """
    divisao = num / 2
    return f'\033[34m{moeda(num)} / 2 = {moeda(divisao)}\033[m'


def moeda(preco, moeda='R$'):
    """
    Retorna meu valor formatado corretamente.
    Substitui o '.', por ','. Como é o correto no português.
    """
    return f'{moeda} {preco:.2f}'.replace('.', ',')


def resumo(preco, aumento, diminui):
    """
    Função que faz o resumo das funções anteriores.
    :param preco: recebe valor recebido pra cálculos matemáticos
    :param aumento: porcentagem de aumento
    :param diminui: porcentagem de redução
    :return: cálculo referente a cada função de dobro, metade, aumento e redução do preço recebido.
    """
    print(f'\033[36mRESUMO DO VALOR RECEBIDO {preco:.2f}\033[m\n')
    dobro = preco * 2
    metade = preco / 2
    aumento = preco + ((aumento / 100) * preco)
    diminui = preco - ((diminui / 100) * preco)

    return f'Dobro do preço: \t{moeda(dobro)}' \
           f'\nMetade: \t{moeda(metade)}' \
           f'\nAumento: \t{moeda(aumento)}' \
           f'\nDiminuindo: \t{moeda(diminui)}.'

    # outra solução é passar os valores como parâmetros para as funções já criadas. Fiz separado apenas como
    # objeto de estudo
