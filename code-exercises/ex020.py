"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
# SHUFFLE -> EMBALHARAR OS ITENS DA LISTA
from random import shuffle

print('SORTEANDO UMA ORDEM DE LISTA')
primeiro_aluno = input('Nome do primeiro aluno: ')
segunda_aluno = input('Nome do segundo aluno: ')
terceiro_aluno = input('Nome do terceiro aluno: ')
quarto_aluno = input('Nome do quarto aluno: ')

lista_de_alunos = [primeiro_aluno, segunda_aluno, terceiro_aluno, quarto_aluno]
shuffle(lista_de_alunos)

print('Ordem de apresentação: {}.'.format(lista_de_alunos))