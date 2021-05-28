"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
print('FUNÇÃO QUE DESCOBRE O MAIOR\n')


def maior(* valores):
    maior_num = menor_num = cont = 0

    for num in valores:
        if cont == 0:
            maior_num = menor_num = num
        else:
            if num > maior_num:
                maior_num = num
            if num < menor_num:
                menor_num = num
        cont += 1

    print(f'O maior valor de: {valores}, é: {maior_num}. \nE o menor, é {menor_num}.\n')

    # outra opção de solução é usar o próprio método do python: max() / min()
    #print(f'O maior valor de: {valores}, é: {max(valores)}.')


maior(1, 2, 3, 4)
maior(4, 3, 2, 1)
maior(6)
maior(0)
maior(9, 100, 12, 15)
