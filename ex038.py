"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""
from emoji import emojize
print('\033[36mCOMPARANDO NUMÉROS\033[m')
num1 = int(input('Digite primeiro número: '))
num2 = int(input('Digite segundo número: '))

# outra opção é usando max() e min(), passando os numéros digitados como parâmetro
if num1 > num2:
    print('O \033[31mprimeiro\033[m valor é maior.')
elif num2 > num1:
    print('O \033[31msegundo\033[m valor é maior.')
else:
    print(emojize('Não existe valor maior, pois são iguais :kiss: ', use_aliases=True))
