"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""
print('ANALISANDO E GERANDO DICIONÁRIOS EM PYTHON\n')


def notas(*notas, situacao=False):
    """
    Função que recebe e calcula várias notas de alunos
    :param notas: recebe uma ou várias notas de alunos
    :param situacao: (opcional), retorna a situação das notas com base na média
    :return: retorna um dicionário com os dados
    """

    qnt_notas = 0  # outra opção é contar len(lista_notas)...
    lista_notas = []

    # varrendo notas, somando a quantidade e adicionando à lista
    for nota in notas:
        qnt_notas += 1
        lista_notas.append(nota)

    # calculando média das notas
    media = sum(lista_notas) / qnt_notas

    # dicionário
    dicionario_notas = {
        'quantidade_notas': qnt_notas,
        'maior_nota': max(lista_notas),
        'menor_nota': min(lista_notas),
        'media_nota': f'{media:.2f}'
    }

    # situação, se receber True, printa situação...
    if situacao:
        if media > 7:
            dicionario_notas['situacao_turma'] = 'ÓTIMO'
        elif media > 5:
            dicionario_notas['situacao_turma'] = 'BOM / REGULAR'
        else:
            dicionario_notas['situacao_turma'] = 'RUIM'

    # retornando dicionário
    return dicionario_notas


print(notas(7, 9, 4, 2, 10, 7, 8, 10, situacao=True))
# print(notas(7, 9, 4, 2, 10, 7, 8, 10, situacao=True))
# help(notas)
