"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários acima de R$ R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
print('AUMENTOS MÚLTIPLOS')

salario = float(input('Qual o salário do funcionário? '))

if salario > 1250:
    calculo_aumento = (salario * 0.1) + salario
    print('Seu salário era de R$ {}, com 10% de aumento, passa a ser R$ {}.'.format(salario, calculo_aumento))
else:
    calculo_aumento = (salario * 0.15) + salario
    print('Seu salário era de R$ {}, com 15% de aumento, passa a ser R$ {}.'.format(salario, calculo_aumento))
