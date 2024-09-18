"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
print('LISTA ORDENADA SEM REPETIÇÕES')

lista = []

for i in range(0, 5):
    numero = int(input(f'Digite {i}° valor: '))

    # -1 porque é o meu último item da lista. Se for o primeiro ou maior que o último item da lista, adicione
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Valor incluso na lista...')
    else:
        # posicao = pra varrer a lista
        posicao = 0

        # enquanto posicao for menor que o comprimento da lista
        while posicao < len(lista):

            # se o número digitado for menor ou igual ao valor da lista na posição, posição, insert o valor.
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Valor incluído na {posicao}° posição da lista...')
                break
            posicao += 1

print(f'Valores em ordem: {lista}.')
