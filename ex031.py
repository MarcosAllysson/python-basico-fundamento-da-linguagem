"""
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
e R$ 0,45 para viagens mais longas.
"""
print('CUSTO DA VIAGEM')

distancia_da_viagem = float(input('Qual a distância da viagem? '))

if distancia_da_viagem >= 200:
    print('Para viagens acima de 200km, como seu caso, deve-se pagar R$ 0,50 por km. '
          'Então você deve pagar R$ {}.'.format(distancia_da_viagem * 0.45))
else:
    print('Para viagens abaixo de 200km, como seu caso, deve-se pagar R$ 0,45 por km. '
          'Então você deve pagar R$ {}.'.format(distancia_da_viagem * 0.50))
