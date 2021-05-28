"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""
print('FICHA DO JOGADOR\n')


def ficha(nome='<desconhedo>', gols=0):
    """
    Função que printa a ficha de um jogador.
    :param nome: recebe string para do nome do jogador (opcional)
    :param gols: quantidade de gols marcado por ele (opcional)
    :return: os dados desse jogador, com ou sem dados fornecidos por completo.
    """
    return f'O jogador {nome} marcou {gols} gols.'


#help(ficha)
jogador = str(input('Qual nome do jogador? ')).strip().title()
gols = str(input('Quantos gols marcou? ')).strip()

if jogador == '' and gols == '':
    print(ficha())
elif jogador == '':
    print(ficha(gols=gols))
elif gols == '':
    print(ficha(nome=jogador))
else:
    print(ficha(jogador, gols))
