"""
Crie um programa que leia 2 valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
print('\033[1;36mCRIANDO UM MENU DE OPÇÕES\033[m')

valor1 = int(input('Digite valor 1: '))
valor2 = int(input('Digite valor 2: '))
opcao = 0

while opcao != 5:
    opcao = int(input('\n{:=^25} \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair \nSua escolha: '
                      .format('MENU')))

    if opcao == 1:
        soma = valor1 + valor2
        print('Soma de {} + {} = {}.'.format(valor1, valor2, soma))

    elif opcao == 2:
        multi = valor1 * valor2
        print('Soma de {} + {} = {}.'.format(valor1, valor2, multi))

    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior entre {} e {}, é {}.'.format(valor1, valor2, maior))

    elif opcao == 4:
        print('Beleza, vamos lá...')
        valor1 = int(input('Digite valor 1: '))
        valor2 = int(input('Digite valor 2: '))

    elif opcao == 5:
        print('Finalizando... até mais =D')

    else:
        print('Opção inválida.')
