"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

print('SALÁRIO')
salario = float(input('Qual salário? '))
calcula_aumento = salario * (15 / 100)
novo_salario = salario + calcula_aumento

print('Antigo salário \033[4;32;40mR$ {}\033[m, com 15% de aumento, o funcionário passa a ganhar R$ {:.2f}.'.format(salario, novo_salario))
