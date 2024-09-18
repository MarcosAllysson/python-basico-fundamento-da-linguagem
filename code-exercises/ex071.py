"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('SIMULADOR DE CAIXA ELETRÔNICO')

cedula50 = cedula20 = cedula10 = cedula1 = 0

valor_saque = int(input('Notas de R$50, R$20, R$10 e R$1 disponível \nQuer sacar quanto? '))

# começa pela maior cédula, e as demais divido pelo resto da divisão por 50, pegando número inteiro da divisão.
cedula50 = valor_saque // 50
cedula20 = (valor_saque % 50) // 20
cedula10 = (valor_saque % 20) // 10
cedula1  = (valor_saque % 10) // 1

#print(f'{cedula50} notas de R$50, \n{cedula20:.0f} notas de R$20, \n{cedula10:.0f} notas de R$10, \n{cedula1:.0f} notas de R$1.')


# solução aula
total = valor_saque
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total_cedula == 0:
            break
