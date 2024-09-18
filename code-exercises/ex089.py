"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
"""
print('BOLETIM COM LISTAS COMPOSTAS')

lista_completa = list()

while True:
    nome = str(input('Nome do aluno(a): ')).title()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media_notas = (nota1 + nota2) / 2

    lista_completa.append([nome, [nota1, nota2], media_notas])
    escolha = str(input('\nQuer adicionar outro aluno(a)? (Sim/Não): ')).strip().upper()[0]
    if escolha == 'N':
        break

print()
print(f'{"N°":<5}{"Nome":<10}{"Média":>8}')
for indice, aluno in enumerate(lista_completa):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    mostrar_nota = int(input('\nQuer ver a nota de qual aluno? \n(999 para parar)! \nSua escolha: '))
    if mostrar_nota == 999:
        print('Ok, saindo...')
        break

    if mostrar_nota <= len(lista_completa) - 1:
        print(f'\nNotas do {lista_completa[mostrar_nota][0]} são respectivamente: {lista_completa[mostrar_nota][1]}')
