"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
"""

print('CALCULA MÉDIA')
primeira_nota = float(input('Nota 1: '))
segunda_nota = float(input('Nota 2: '))
media = (primeira_nota + segunda_nota) / 2

#print('A média do aluno é {:=^10.2f}.'.format((primeira_nota + segunda_nota) / 2))
print('A média do aluno é {:=^10.1f}'.format(media))
