"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiscúlas
- O nome com todas as letras minúsculas
- Quantos letras ao todos (sem considerar espaços)
- Quantas letras têm o primeiro nome.
"""

print('ANALISADOR DE TEXTO')
nome_completo = str(input('Qual seu nome completo: '))
letras_maisculas = nome_completo.upper()
letras_minusculas = nome_completo.lower()

# tiro todos os espaços da direita e esquerda, quebro a string numa lista, junto cada índice e conto a quantidade.
letras_total = len(''.join(nome_completo.strip().split(' ')))

# tiro todos os espaços da direita e esquerda, quebro a string numa lista, conto a quantidade do 1° índice da lista.
letras_primeiro_nome = len(nome_completo.strip().split(' ')[0])

#outra opção pra contar os espaços. Subtraio o tamanho de tudo menos quantos espaço contém.
#letras_total_aula = len(nome_completo) - nome_completo.count(' ')

print('Certo, vamos lá. Nome completo: {} '
      '\nO nome com todas as letras maiscúlas: {};'
      '\nO nome com todas as letras minúsculas: {};'
      '\nQuantos letras ao todos (sem considerar espaços): {} letras;'
      '\nPrimeiro nome têm {} letras.'.format(nome_completo, letras_maisculas, letras_minusculas, letras_total, letras_primeiro_nome))
