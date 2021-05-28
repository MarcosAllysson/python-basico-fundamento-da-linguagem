"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
print('LISTA COM PARES E ÍMPARES\n')

numeros = list()
numeros_pares = list()
numeros_impares = list()
numeros_temporarios = list()

for i in range(0, 7):
    # pedindo valores e adicionando à lista temporária
    numeros_temporarios.append(int(input(f'Digite {i+1}° número: ')))

    # verificando se é par e adicionando à lista dos pares
    if numeros_temporarios[0] % 2 == 0:
        numeros_pares.append(numeros_temporarios[0])
    # se não par, adiciona à lista dos ímpares
    else:
        numeros_impares.append(numeros_temporarios[0])

    # limpando valores da lista temporária
    numeros_temporarios.clear()


# adicionando pares e ímpares à lista geral
numeros.append(numeros_pares)
numeros.append(numeros_impares)

# ordenando em ordem crescente
numeros[0].sort()
numeros[1].sort()

# printando lista completa
print(f'Números pares{numeros[1]}, e os ímpares: {numeros[0]}')



# outra solução, é criar uma lista, com duas listas. Se for par, índice 0 recebe os números, e índice 1, os ímpares.
