"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
from time import sleep
print('\033[31mDIVIDINDO VALORES EM VÁRIAS LISTAS\033[m \n')

# criação de 3 listas vazias.
lista = []
lista_pares = []
lista_impares = []

while True:
    lista.append(int(input('\033[36mAdicione um valor à lista\033[m: ')))
    escolha = str(input('\nInserir outro? (Sim/Não)? ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'\nAnalisando pares e ímpares da sua lista: {lista}...')
sleep(2)

# varrendo lista, verificando ímpar ou par e adicionando a respectiva lista.
for item in lista:
    if item % 2 == 0:
        lista_pares.append(item)
    else:
        lista_impares.append(item)

print(f'\n \033[35mPronto!\033[m \nLista somente dos pares: {lista_pares}. \nÍmpares: {lista_impares}.')
