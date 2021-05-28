"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import randint, choice

print('SORTEANDO UM ITEM NA LISTA')
primeiro_aluno = input('Nome do primeiro aluno: ')
segundo_aluno = input('Nome do segundo aluno: ')
terceiro_aluno = input('Nome do tereceiro aluno: ')
quarto_aluno = input('Nome do quarto aluno: ')

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
numero_aleatorio = randint(0, 3)
# outra opção
#aluno_escolhido = choice(lista)
aluno_escolhido = lista[numero_aleatorio]

print('O aluno escolhido foi o \033[1;36m{}.\033[m'.format(aluno_escolhido))
