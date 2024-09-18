"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
"""
print('MAIOR E MENOR VALORES NA LISTA')

lista = []
maior = menor = 0
maiorlist = []
menorlist = []

for i in range(0, 5):
    lista.append(int(input(f'Digite o {i}° valor da lista: ')))

    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

# varrendo a lista e vendo posições do maior e menor número digitado adicionando à lista respectivamente.
for posicao, valor in enumerate(lista):
    if valor == maior:
        maiorlist.append(posicao)
    if valor == menor:
        menorlist.append(posicao)

print(f'\nValores digitados foram os: {lista}.')
# print(f'Maior valor digitado foi o {max(lista)}, na {lista.index(max(lista))}° posição.')
# print(f'Maior valor digitado foi o {maior}, nas posições: ', end='')

print(f'Maior valor digitado foi o {maior}, nas posições: {maiorlist}')
# varrendo a lista e vendo posições do maior número digitado
# for posicao, valor in enumerate(lista):
#    if valor == maior:
#        print(f'{posicao}', end=', ')


# print(f'E o menor foi {min(lista)}, na {lista.index(min(lista))}° posição.')
# print(f'\nE o menor foi {menor}, nas posições: ', end=' ')

print(f'\nE o menor foi {menor}, nas posições: {menorlist}')
# varrendo a lista e vendo posições do menor número digitado
# for posicao, valor in enumerate(lista):
#    if valor == menor:
#        print(f'{posicao}', end=', ')
