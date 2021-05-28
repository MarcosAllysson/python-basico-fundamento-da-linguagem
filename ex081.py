"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
print('EXTRAINDO DADOS DE UMA LISTA')

lista = []
cont = 0

while True:
    lista.append(int(input('Adicione um número à lista: ')))
    cont += 1
    escolha = str(input('Quer inserir outro? (Sim/Não)? ')).strip().upper()[0]

    if escolha == 'N':
        break

# outra solução: len(lista)
print(f'Foram digitados: {cont} números.')

# ordenando a lista de forma decrescente
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}.')

# verificando se o valor 5 está ou não na lista.
if 5 in lista:
    print(f'O valor 5 está na {lista.index(5)}° posição.')
else:
    print('O número 5 não foi inserido à lista.')
