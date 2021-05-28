"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""
print('VALORES ÚNICOS EM UMA LISTA')

lista = []

while True:
    numeros = int(input('Digite um valor: '))
    if numeros not in lista:
        lista.append(numeros)
        print('Valor incluso...')
    else:
        print('Número existente e não foi adicionado à lista. ')

    escolha = str(input('Quer continuar? (Sim/Não): ')).strip().upper()[0]

    if escolha == 'N':
        break

print(f'\nValores adicionados: {lista}')

# colocando a lista em crescente.
lista.sort()
print(f' agora, em ordem crescente: {lista}')
