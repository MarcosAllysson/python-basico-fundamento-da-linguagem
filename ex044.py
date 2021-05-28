"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""
print('\033[31mGERENCIADOR DE PAGAMENTOS\033[m')
valor = float(input('Valor a ser pago no produto: R$ '))
forma_pagamento = int(input('Selecione a forma de pagamento: \n1 - À vista no dinheiro / cheque'
                            '\n2 - À vista no cartão'
                            '\n3 - Em até 2x no cartão'
                            '\n4 - 3x ou mais no cartão'
                            '\nComo prefere pagar: '))

if forma_pagamento == 1:
    a_vista_dinheiro = valor - (valor * 0.1)
    print('Pagando à vista no dinheiro ou cheque você tem 10% de desconto, o novo preço é R$ {:.2f}'.format(a_vista_dinheiro))
elif forma_pagamento == 2:
    a_vista_cartao = valor - (valor * 0.05)
    print('Pagando no cartão tens 5% de desconto, o novo preço é R$ {:.2f}'.format(a_vista_cartao))
elif forma_pagamento == 3:
    cartao_2x = valor / 2
    print('Em até 2x no cartão, preço normal em duas parcelas de R$ {:.2f}'.format(cartao_2x))
elif forma_pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    cartao_3x = valor + (valor * 0.2)
    print('Em {} parcelas somados 20% de juros, custará R$ {:.2f}'.format(parcelas, cartao_3x / 3))
else:
    print('\033[35mOpção inválida.\033[m')
