"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
from time import sleep
print('ESTATÍSTICAS EM PRODUTOS')

total_gasto = produtos_acima_1000 = mais_barato = cont_produto = 0
nome_mais_barato = ' '
continuar = False

while continuar != True:
    print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    nome = str(input('Qual nome do produto? '))
    preco = float(input('Qual preço do produto? R$ '))
    escolha = ' '

    # somando total gasto na compra
    total_gasto += preco

    # produtos que custam mais de R$ 1000
    if preco > 1000:
        produtos_acima_1000 += 1

    # produto mais barato sendo contabilizado e verificado
    cont_produto += 1

    # se o produto for o 1° digitado, mais barato recebe preço. Se não, comparo se preço é menor que o mais barato.
    if cont_produto == 1 or preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome
    #else:
    #    if preco < mais_barato:
    #        mais_barato = preco
    #        nome_mais_barato = nome

    # verificando se quer continuar ou não
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? (SIM/NÃO)? ')).strip().upper()[0]

    # se não quiser continuar, recebe True e o programa para.
    if escolha == 'N':
        continuar = True

print('\nFechando caixa...')
sleep(2)
print(f'Total gasto de compra R$ {total_gasto:.2f}, dos quais {produtos_acima_1000} custam acima de R$ 1.000,00,'
      f' o produto mais barato custa R$ {mais_barato}, que é o {nome_mais_barato}.')
