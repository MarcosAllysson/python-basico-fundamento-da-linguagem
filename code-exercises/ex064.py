"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag 'condição de parada').
"""
print('TRATANDO VÁRIOS VALORES')

# outra opção
# numeros = cont_num = soma_num = 0
numeros = 0
cont_num = 0
soma_num = 0
numeros = int(input('Digite valor: '))

while numeros != 999:
    cont_num += 1
    soma_num += numeros
    numeros = int(input('Digite valor: '))

print('{} números digitados. Soma entre eles vale {}.'.format(cont_num, soma_num))
