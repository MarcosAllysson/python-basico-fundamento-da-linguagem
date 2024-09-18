"""
Faça um programa que leia um nuḿero de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo: número 1834
unidade: 4, dezena: 3, centena: 8 e milhar: 1.
"""

print('SEPARANDO DÍGITOS DE UM NÚMERO')
numero = int(input('Digite um número: '))
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = (numero % 10) // 1
print('\033[4;31mNúmero {},\033[m'
      '\nMilhar: {},'
      '\nCentena: {},'
      '\nDezena: {},'
      '\nUnidade: {}.'.format(numero, milhar, centena, dezena, unidade))

# outra opção é converter o número pra str e printar os índices 0,1,2,3.