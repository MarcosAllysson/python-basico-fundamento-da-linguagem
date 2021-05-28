"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
print('LISTA COMPOSTA E ANÁLISE DE DADOS')

temporaria = list()
pessoas = list()
mais_pesada = mais_leve = 0

while True:
    temporaria.append(str(input('Digite o nome: ')))
    temporaria.append(float(input('Digite o peso: KG ')))

    # adicionando e verificando mais leve e pesado
    if len(pessoas) == 0:
        mais_leve = mais_pesada = temporaria[1]
    else:
        if temporaria[1] > mais_pesada:
            mais_pesada = temporaria[1]
        if temporaria[1] < mais_leve:
            mais_leve = temporaria[1]

    # gerando cópia da lista temporária e adicionando à lista pessoas
    pessoas.append(temporaria[:])

    # limpando lista
    temporaria.clear()

    escolha = str(input('\nQuer inserir outra? (Sim/Não)? ')).strip().upper()[0]
    if escolha == 'N':
        break

print('=='*30)
# print(f'Pessoas adicionadas: {pessoas}.')
print(f'Foram cadastrados {len(pessoas)} pessoas.')

# varrendo a lista pra encontrar os mais pesados
print(f'O mais pesado tem {mais_pesada}Kg, e são: ', end='')
for pessoa in pessoas:
    if pessoa[1] == mais_pesada:
        print(pessoa[0], end='')

# varrendo a lista pra encontrar os mais pesados
print(f'E o mais leve tem {mais_leve}Kg, e são: ', end='')
for pessoa in pessoas:
    if pessoa[1] == mais_leve:
        print(pessoa[0], end='')
