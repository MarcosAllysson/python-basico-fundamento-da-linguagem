"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
print('DICIONÁRIO EM PYTHON\n')

aluno = {}

aluno['nome'] = str(input('Nome do aluno: ')).strip().title()
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['media'] >= 6:
    aluno['situacao'] = 'Aluno aprovado com sucesso!'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Aluno em recuperação'
else:
    aluno['situacao'] = 'Aluno reprovado =('

#print(aluno.items())
print()
for chave, valor in aluno.items():
    print(f'{chave}: {valor}.')
