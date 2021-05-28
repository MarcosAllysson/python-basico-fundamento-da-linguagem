"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
print('Detector de Palíndromo'.upper())

# já tiro espaços e formo lista
frase_normal = str(input('Escreva uma frase: '))
frase = frase_normal.strip().lower().split(' ')

# após espaços em branco tirados e lista formada, variável recebe pra cada item da lista, juntando com nada ''
frase_convertida = ''.join(frase)

# variável recebe frase de trás pra frente. Começa no primeiro, até o final, mas de trás pra frente.
verifica_palindromo = frase_convertida[::-1]

if frase_convertida == verifica_palindromo:
    print('\033[31m{}\033[m, \033[4mé palíndromo.\033[m'.format(frase_normal))
else:
    print('\033[36m{}\033[m, \033[1;31mnão é palíndromo.\033[m'.format(verifica_palindromo))
