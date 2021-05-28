"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'a'
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece por último.
"""

print('PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING')

#setando string pra minúsculo e já tirando espaços em branco da esquerda e direita.
frase = str(input('Digite sua frase: ')).lower().strip()
qnt_a = frase.count('a')

#retorna primeira aparição da letra 'a' na frase somando a 1 pra que fique similar a leitura humana.
primeira_posicao_a = frase.find('a')+1

#começando da última posição, retorna a posição no índice que contém a letra 'a'.
#ultima_posicao_a = frase[::-1].find('a')
ultima_posicao_a = frase.rfind('a')+1

print('Frase digitada: {},'
      '\nLetras "a" aparecem {} vezes,'
      '\nPrimeiro aparece na posição {},'
      '\ne aparece por último na posição {}.'.format(frase, qnt_a, primeira_posicao_a, ultima_posicao_a))
