"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
from time import sleep
print('\033[35mANALISADOR COMPLETO\033[m')

idade_total = 0
cont_mulher = 0
maior_p_homem = 0
maior_p_nome = ''
media = 0

for i in range(1, 5):
    nome = str(input('\033[31mNome\033[m da {}° pessoa: '.format(i))).strip()
    idade = int(input('\033[31mIdade\033[m da {}° pessoa: '.format(i)))
    sexo = int(input('Qual \033[31msexo\033[m da {}° pessoa: \n1 - Homem \n2 - Mulher \nSua opção: '.format(i)))

    # Se for homem, comparo se idade > que 0, se for, maior idade recebe idade e nome. Senão, faz nada.
    if sexo == 1:
        if idade > maior_p_homem:
            maior_p_homem = idade
            maior_p_nome = nome

    # Se for mulher, comparo se idade < que 20, se for, variável cont recebe mais
    elif sexo == 2:
        if idade < 20:
            cont_mulher += 1

    # Se não for mulher ou homem, apenas printa opção inválida...
    else:
        print('Opção inválida...')

    # Somando todas as idades.
    idade_total += idade #somando todas as idades


# calculando média de idade
print()
print('Calculando média de idade das pessoas...')
media = idade_total / 4
sleep(1)

print('Analisando quantas mulheres têm abaixo de 20 anos...')
sleep(1)

print('Verificando homem mais velho...')
sleep(1)

print()
print('\033[4mMédia de idade\033[m do grupo: {};'
      '\nMulheres \033[4mabaixo de 20 anos\033[m: {};'
      '\nO \033[4mhomem mais velho\033[m se chama {} e tem {} anos.'.format(media, cont_mulher, maior_p_nome, maior_p_homem))
