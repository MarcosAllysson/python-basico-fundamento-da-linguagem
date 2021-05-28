"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('APROVANDO EMPRÉSTIMO')
valor_casa = float(input('Qual valor da casa? R$ '))
valor_salario = float(input('Qual o salário? R$ '))
anos_pagamento = int(input('Quantos anos vai pagar? '))

#calculando prestação mensal dividindo valor da casa pelo meses
prestacao_mensal = valor_casa / (anos_pagamento * 12)

#calculando 30% do salário
porcentagem_pagamento = valor_salario * 0.3

#cálculo do empréstimo
if prestacao_mensal <= porcentagem_pagamento:
    print('Ótimo, empréstimo concecido com \033[1;36msucesso.\033[m')
    print('Valor da casa R$ {},'
          'salário R$ {},'
          'vai pagar em {} anos.'
          '\nPrestação mensal R${:.2f}.'.format(valor_casa, valor_salario, anos_pagamento, prestacao_mensal))
else:
    print('\033[1;31mEmpréstimo negado, motivo\033[m: a parcela de R$ {:.2f} excede 30% do seu salário. '
          'Considere ganhar mais!'.format(prestacao_mensal))
