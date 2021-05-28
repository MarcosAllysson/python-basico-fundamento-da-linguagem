"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.
"""
from emoji import emojize

print('RADAR ELETRÔNICO')

cores = {
    'azul_claro': '\033[1;36m',
    'fundo': '\033[0;30;42m'
}

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    excedido = velocidade - 80
    calcula_multa = (velocidade - 80) * 7
    print(emojize('Você foi multado :anger: :rotating_light: . '
                  'Valor da multa é de R$ 7,00 por km excedido.'
                  'Você ultrapassou {}km, '
                  'então pague a multa de {}R$ {:.0f},00'.format(excedido, cores['azul_claro'], calcula_multa), use_aliases=True))
else:
    print('De boa, continue assim...')

print('Tenha um {}ótimo dia e {}fique com Deus.'.format(cores['azul_claro'], cores['fundo']))
